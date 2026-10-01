# flock_routes.py - COMPLETE REVISION v3
from flask import Blueprint, request, session, redirect, url_for, flash, render_template_string, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from db_ext import db
from sqlalchemy import func
from datetime import date, datetime, timedelta
from functools import wraps
import json
import re
import random
from flock_models import (
    User, FlockBatch, Vaccine, VaccinationRecord, MedicationSchedule,
    MortalityRecord, WeightRecord, AdgCalculation, FcrCalculation, FlockReport,
    MarketPrice, FeedRecord, DailyFeedRecord,
    ExpenseCategory, WaterExpense, ElectricityExpense, OtherExpense,
    PerformanceReport, Vitamin, VitaminSchedule, LpgExpense, LaborExpense,
    HarvestHistory, HarvestSale, DailyRecordSubmission,
    VaccineExpense, FeedExpense,
)
from flock_templates import (
    TEMPLATE_LOGIN, TEMPLATE_OWNER, TEMPLATE_MANAGER, TEMPLATE_WORKER,
    TEMPLATE_PERFORMANCE_REPORT_PRINT
)

bp = Blueprint("main", __name__)

MONTH_ORDER = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
FEED_CATEGORIES = ["Chick Booster", "Grower Pellets", "Finisher Pellets"]
SEASONS = ["Dry", "Wet"]
FEED_NUTRIENT_FIELDS = [
    "crude_protein", "crude_fat", "crude_fiber",
    "moisture", "calcium", "phosphorus",
]

# ─── Auth Decorators ────────────────────────────────────────────────────────

def login_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in first.")
            return redirect(url_for("main.login"))
        return f(*args, **kwargs)
    return wrapped

def role_required(*roles):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if session.get("role") not in roles:
                flash("Access denied.")
                return redirect(url_for("main.dashboard"))
            return f(*args, **kwargs)
        return wrapped
    return decorator

# ─── Reference / Market Data ────────────────────────────────────────────────

BANTAY_PRESYO_URL = "https://www.bantaypresyo.da.gov.ph/tbl_meat.php"
BANTAY_PRESYO_FALLBACK_PRICE = 165.0

def get_da_bantay_presyo_price():
    try:
        import requests
        from bs4 import BeautifulSoup
    except ImportError:
        return {"price": BANTAY_PRESYO_FALLBACK_PRICE, "source": "Fallback reference (scraper libraries not installed)", "live": False}

    try:
        resp = requests.get(BANTAY_PRESYO_URL, timeout=6)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        chicken_prices = []
        for row in soup.find_all("tr"):
            cells = [c.get_text(strip=True) for c in row.find_all(["td", "th"])]
            if len(cells) < 2:
                continue
            label = cells[0].lower()
            if "chicken" not in label and "manok" not in label:
                continue
            for cell in cells[1:]:
                cleaned = cell.replace(",", "").replace("₱", "").replace("php", "").strip()
                try:
                    val = float(cleaned)
                except ValueError:
                    continue
                if 50.0 <= val <= 500.0:
                    chicken_prices.append(val)

        if chicken_prices:
            avg_price = round(sum(chicken_prices) / len(chicken_prices), 2)
            return {"price": avg_price, "source": "DA Bantay Presyo (live)", "live": True}
    except Exception:
        pass

    return {"price": BANTAY_PRESYO_FALLBACK_PRICE, "source": "Fallback reference (live page unavailable)", "live": False}

def get_live_market_data():
    scraped = get_da_bantay_presyo_price()
    return {
        "retail_avg": scraped["price"],
        "last_update": date.today().strftime("%b %d, %Y"),
        "source": scraped["source"],
        "live": scraped["live"]
    }

def get_current_avg_market_price():
    return get_live_market_data()["retail_avg"]

# ─── Batch Snapshot ──────────────────────────────────────────────────────────

def get_batch_snapshot(batch):
    latest_weight = (WeightRecord.query.filter_by(batch_id=batch.batch_id)
                      .order_by(WeightRecord.record_date.desc(), WeightRecord.weight_id.desc()).first())
    latest_adg = (AdgCalculation.query.filter_by(batch_id=batch.batch_id)
                  .order_by(AdgCalculation.record_date.desc(), AdgCalculation.calc_id.desc()).first())
    latest_fcr = (FcrCalculation.query.filter_by(batch_id=batch.batch_id)
                  .order_by(FcrCalculation.fcr_id.desc()).first())
    total_feed = db.session.query(func.sum(DailyFeedRecord.total_kg)).filter_by(batch_id=batch.batch_id).scalar() or 0.0

    latest_weight_g = latest_weight.total_weight_gain if latest_weight else 0.0
    age_days = latest_adg.number_of_days if latest_adg else max(0, (date.today() - batch.start_date).days)
    adg_value = latest_adg.adg_value if latest_adg else 0.0
    fcr_value = latest_fcr.fcr_value if latest_fcr else 0.0
    record_date = latest_weight.record_date if latest_weight else batch.start_date

    return {
        "latest_weight_g": latest_weight_g, "age_days": age_days, "adg_value": adg_value,
        "fcr_value": fcr_value, "total_feed": round(total_feed, 2), "record_date": record_date
    }

def get_flock_totals(flocks):
    initial = sum(f.initial_bird_count for f in flocks)
    remaining = sum(f.current_bird_count for f in flocks)
    deaths = max(0, initial - remaining)
    survival_pct = round((remaining / initial) * 100, 1) if initial > 0 else 0.0
    mortality_pct = round((deaths / initial) * 100, 1) if initial > 0 else 0.0
    return {"initial": initial, "remaining": remaining, "deaths": deaths,
            "survival_pct": survival_pct, "mortality_pct": mortality_pct}

# ─── Analytics Helpers ──────────────────────────────────────────────────────

def get_flock_analytics(flocks):
    analytics_list = []
    for f in flocks:
        snap = get_batch_snapshot(f)
        analytics_list.append({
            "flock": f,
            "analytics": {
                "adg": snap["adg_value"],
                "fcr": snap["fcr_value"],
                "latest_weight": snap["latest_weight_g"],
                "age_days": snap["age_days"],
                "total_feed": snap["total_feed"]
            }
        })
    return analytics_list

def get_or_create_category(name):
    cat = ExpenseCategory.query.filter(func.lower(ExpenseCategory.category_name) == name.lower()).first()
    if not cat:
        cat = ExpenseCategory(user_id=session["user_id"], category_name=name)
        db.session.add(cat)
        db.session.flush()
    return cat

def parse_expense_date(form):
    raw = form.get("expense_date")
    if raw:
        try:
            return datetime.strptime(raw, "%Y-%m-%d").date()
        except ValueError:
            pass
    return date.today()

def get_active_batch():
    """Return the single active batch, or None."""
    return FlockBatch.query.filter_by(flock_status="Active").first()

def get_category_spending(year=None, month=None):
    today = date.today()
    year = year or today.year
    month = month or today.month

    def month_totals(model, amount_col):
        return (db.session.query(ExpenseCategory.category_name, func.sum(amount_col))
                .join(model, model.expense_category_id == ExpenseCategory.expense_category_id)
                .filter(func.extract('year', model.expense_date) == year,
                        func.extract('month', model.expense_date) == month)
                .group_by(ExpenseCategory.category_name)
                .all())

    totals = {}
    for model, amount_col in [
        (WaterExpense, WaterExpense.water_expense_amount),
        (ElectricityExpense, ElectricityExpense.electricity_expense_amount),
        (LpgExpense, LpgExpense.lpg_expense_amount),
        (LaborExpense, LaborExpense.labor_expense_amount),
        (OtherExpense, OtherExpense.other_expense_amount),
    ]:
        for cat_name, amt in month_totals(model, amount_col):
            totals[cat_name] = totals.get(cat_name, 0.0) + (amt or 0.0)

    rows = sorted(
        ({"category": k, "total": round(v, 2)} for k, v in totals.items()),
        key=lambda r: r["total"], reverse=True
    )
    return {
        "year": year,
        "month": month,
        "month_value": f"{year:04d}-{month:02d}",
        "month_label": date(year, month, 1).strftime("%B %Y"),
        "rows": rows,
        "grand_total": round(sum(r["total"] for r in rows), 2)
    }

def get_expense_summary():
    water_total = db.session.query(func.sum(WaterExpense.water_expense_amount)).scalar() or 0.0
    elec_total = db.session.query(func.sum(ElectricityExpense.electricity_expense_amount)).scalar() or 0.0
    lpg_total = db.session.query(func.sum(LpgExpense.lpg_expense_amount)).scalar() or 0.0
    labor_total = db.session.query(func.sum(LaborExpense.labor_expense_amount)).scalar() or 0.0
    other_total = db.session.query(func.sum(OtherExpense.other_expense_amount)).scalar() or 0.0
    vaccine_total = db.session.query(func.sum(VaccineExpense.vaccine_expense_amount)).scalar() or 0.0
    feed_total = db.session.query(func.sum(FeedExpense.feed_expense_amount)).scalar() or 0.0

    return {
        "water": round(water_total, 2),
        "electricity": round(elec_total, 2),
        "lpg": round(lpg_total, 2),
        "labor": round(labor_total, 2),
        "other": round(other_total, 2),
        "vaccine": round(vaccine_total, 2),
        "feed": round(feed_total, 2),
        "total": round(water_total + elec_total + lpg_total + labor_total + other_total + vaccine_total + feed_total, 2)
    }

def get_profit_loss_summary():
    total_revenue = db.session.query(func.sum(HarvestSale.total_amount)).scalar() or 0.0
    total_expenses = get_expense_summary()["total"]
    net = round(total_revenue - total_expenses, 2)
    return {
        "total_revenue": round(total_revenue, 2),
        "total_expenses": total_expenses,
        "net": net,
        "status": "Profit" if net >= 0 else "Loss",
        "has_sales": total_revenue > 0
    }

def get_harvest_profit_summary():
    harvests = HarvestHistory.query.all()
    total_batch_expenses = sum(h.expenses or 0.0 for h in harvests)
    total_profit = sum(h.loss_gain or 0.0 for h in harvests)
    total_revenue = total_profit + total_batch_expenses
    return {
        "batch_count": len(harvests),
        "total_revenue": round(total_revenue, 2),
        "total_batch_expenses": round(total_batch_expenses, 2),
        "total_profit": round(total_profit, 2),
        "status": "Profit" if total_profit >= 0 else "Loss"
    }

def get_upcoming_schedule(days_ahead=7):
    now = datetime.utcnow()
    end = now + timedelta(days=days_ahead)
    lookback = now - timedelta(days=2)

    vaccinations = (VaccinationRecord.query
        .filter(VaccinationRecord.status == 'Scheduled',
                VaccinationRecord.scheduled_date <= end,
                VaccinationRecord.scheduled_date >= lookback)
        .order_by(VaccinationRecord.scheduled_date).all())

    vitamins = (VitaminSchedule.query
        .filter(VitaminSchedule.status == 'Scheduled',
                VitaminSchedule.scheduled_date <= end,
                VitaminSchedule.scheduled_date >= lookback)
        .order_by(VitaminSchedule.scheduled_date).all())

    items = []
    for v in vaccinations:
        items.append({
            "kind": "Vaccination", "label": v.vaccine.vaccine_name if v.vaccine else "Vaccine",
            "batch": v.batch.batch_name if v.batch else "-", "date": v.scheduled_date,
            "overdue": v.scheduled_date < now, "id": v.vaccination_record_id,
            "icon": "fa-syringe"
        })
    for v in vitamins:
        items.append({
            "kind": "Vitamin", "label": v.vitamin.vitamin_name if v.vitamin else "Vitamin",
            "batch": v.batch.batch_name if v.batch else "-", "date": v.scheduled_date,
            "overdue": v.scheduled_date < now, "id": v.schedule_id,
            "icon": "fa-tablets"
        })
    items.sort(key=lambda i: i["date"])
    return items

def get_today_tasks():
    now = datetime.utcnow()
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    today_end = today_start + timedelta(days=1)

    vaccinations = (VaccinationRecord.query
        .filter(VaccinationRecord.status == 'Scheduled',
                VaccinationRecord.scheduled_date >= today_start,
                VaccinationRecord.scheduled_date < today_end)
        .all())

    vitamins = (VitaminSchedule.query
        .filter(VitaminSchedule.status == 'Scheduled',
                VitaminSchedule.scheduled_date >= today_start,
                VitaminSchedule.scheduled_date < today_end)
        .all())

    tasks = []
    for v in vaccinations:
        tasks.append({
            "title": v.vaccine.vaccine_name if v.vaccine else "Vaccination",
            "type": "Vaccination",
            "batch": v.batch.batch_name if v.batch else "-",
            "date": v.scheduled_date,
            "icon": "fa-syringe"
        })
    for v in vitamins:
        tasks.append({
            "title": v.vitamin.vitamin_name if v.vitamin else "Vitamin",
            "type": "Vitamin",
            "batch": v.batch.batch_name if v.batch else "-",
            "date": v.scheduled_date,
            "icon": "fa-tablets"
        })
    return tasks

def get_day12_vaccine():
    v = VaccinationRecord.query.filter_by(status='Scheduled').first()
    return v.vaccine.vaccine_name if v and v.vaccine else None

def get_day16_vaccine():
    v = VaccinationRecord.query.filter_by(status='Scheduled').offset(1).first()
    return v.vaccine.vaccine_name if v and v.vaccine else None

# ─── Sales Forecast ─────────────────────────────────────────────────────────

def get_monthly_sales_forecast():
    harvests = HarvestHistory.query.all()
    if len(harvests) < 10:
        return {"available": False, "reason": "Not enough harvest data yet. Need at least 10 batches.", "sample_count": len(harvests)}

    monthly_revenues = {}
    for h in harvests:
        month = h.end_date.strftime("%b") if h.end_date else "Jan"
        monthly_revenues.setdefault(month, []).append(h.loss_gain or 0)

    labels = [m for m in MONTH_ORDER if m in monthly_revenues]
    monthly_sales = [round(sum(monthly_revenues[m]) / len(monthly_revenues[m]), 2) for m in labels]
    best_idx = monthly_sales.index(max(monthly_sales)) if monthly_sales else 0

    return {
        "available": True,
        "labels": labels,
        "monthly_sales": monthly_sales,
        "best_month": labels[best_idx] if labels else "—",
        "best_value": monthly_sales[best_idx] if monthly_sales else 0,
        "sample_count": len(harvests)
    }

# ─── Batch Name Generator ───────────────────────────────────────────────────

def generate_batch_name(custom_suffix):
    year = date.today().year
    existing = FlockBatch.query.filter(
        FlockBatch.batch_name.like(f"Batch-{year}-%")
    ).all()
    used_letters = set()
    for b in existing:
        m = re.match(rf"Batch-{year}-([A-Z])", b.batch_name or "")
        if m:
            used_letters.add(m.group(1))
    letter = next((c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if c not in used_letters), "Z")
    suffix = (custom_suffix or "").strip()
    base = f"Batch-{year}-{letter}"
    return f"{base} {suffix}".strip() if suffix else base

# ─── Worker Daily Submission ───────────────────────────────────────────────

def record_growth_data(batch, user_id, record_date, avg_weight_g, feed_kg, feed_record_id, mortality, cull, cause):
    db.session.add(MortalityRecord(batch_id=batch.batch_id, user_id=user_id, death_count=mortality,
                                    cull_count=cull, cause=cause, record_date=record_date))

    if feed_record_id:
        feed_obj = FeedRecord.query.get(feed_record_id)
        feed_cost = (feed_obj.cost_per_kg * feed_kg) if feed_obj else 0.0
        db.session.add(DailyFeedRecord(batch_id=batch.batch_id, feed_record_id=feed_record_id,
                                        record_date=record_date, total_kg=feed_kg,
                                        total_cost=round(feed_cost, 2)))
        # Auto-log feed expense
        if feed_cost > 0:
            db.session.add(FeedExpense(
                feed_record_id=feed_record_id,
                batch_id=batch.batch_id,
                feed_expense_amount=round(feed_cost, 2),
                feed_expense_status="Paid",
                expense_date=record_date,
                description=f"Feed {feed_obj.feed_name} — {feed_kg}kg"
            ))

    batch.current_bird_count = max(0, batch.current_bird_count - mortality - cull)
    db.session.flush()

    age_days = max(0, (record_date - batch.start_date).days)

    first_w = (WeightRecord.query.filter_by(batch_id=batch.batch_id)
               .order_by(WeightRecord.record_date.asc(), WeightRecord.weight_id.asc()).first())
    starting_weight = first_w.total_weight_gain if first_w else 0.0
    adg_value = round((avg_weight_g - starting_weight) / age_days, 2) if age_days > 0 else 0.0
    adg = AdgCalculation(batch_id=batch.batch_id, user_id=user_id, starting_weight=starting_weight,
                          ending_weight=avg_weight_g, number_of_days=age_days,
                          record_date=record_date, adg_value=adg_value)
    db.session.add(adg)

    total_feed = db.session.query(func.sum(DailyFeedRecord.total_kg)).filter_by(batch_id=batch.batch_id).scalar() or 0.0
    total_weight_kg = round((avg_weight_g * batch.current_bird_count) / 1000.0, 2)
    fcr_value = round(total_feed / total_weight_kg, 2) if total_weight_kg > 0 else 0.0
    fcr = FcrCalculation(batch_id=batch.batch_id, user_id=user_id, total_feed_intake=round(total_feed, 2),
                          total_weight_gain=total_weight_kg, fcr_value=fcr_value)
    db.session.add(fcr)

    db.session.add(WeightRecord(batch_id=batch.batch_id, user_id=user_id, record_date=record_date,
                                 total_weight_gain=avg_weight_g, fcr_value=fcr_value))

    db.session.flush()

    db.session.add(FlockReport(batch_id=batch.batch_id, user_id=user_id,
                                adg_id=adg.calc_id, fcr_id=fcr.fcr_id, report_date=record_date))
    db.session.commit()
    return adg, fcr

def calculate_age(birth_date):
    today = date.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

def redirect_dashboard():
    role = session.get("role")
    if role == "Owner":
        return redirect(url_for("main.owner_dashboard"))
    if role == "Manager":
        return redirect(url_for("main.manager_dashboard"))
    return redirect(url_for("main.worker_dashboard"))

# ─── Auth Routes ────────────────────────────────────────────────────────────

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = User.query.filter_by(username=request.form["username"]).first()
        if u and check_password_hash(u.password_hash, request.form["password"]):
            if not u.is_active:
                flash("This account has been deactivated. Contact the Owner.")
                return render_template_string(TEMPLATE_LOGIN)
            session.update({"user_id": u.user_id, "role": u.role, "full_name": u.full_name})
            return redirect(url_for("main.dashboard"))
        flash("Invalid credentials.")
    return render_template_string(TEMPLATE_LOGIN)

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("main.login"))

# ─── Dashboard Routes ───────────────────────────────────────────────────────

@bp.route("/")
@bp.route("/dashboard")
@login_required
def dashboard():
    role = session.get("role")
    if role == "Owner": return redirect(url_for("main.owner_dashboard"))
    if role == "Manager": return redirect(url_for("main.manager_dashboard"))
    return redirect(url_for("main.worker_dashboard"))

@bp.route("/owner")
@login_required
@role_required("Owner")
def owner_dashboard():
    active_flocks = FlockBatch.query.filter_by(flock_status='Active').all()
    all_flocks = FlockBatch.query.order_by(FlockBatch.batch_id.desc()).all()
    totals = get_flock_totals(active_flocks)
    avg_market = get_current_avg_market_price()

    harvest_data = HarvestHistory.query.order_by(HarvestHistory.end_date.desc()).all()

    # Sort option for harvest history
    sort = request.args.get("sort", "highest")
    if sort == "lowest":
        harvest_data_sorted = sorted(harvest_data, key=lambda h: h.loss_gain or 0)
    else:
        harvest_data_sorted = sorted(harvest_data, key=lambda h: h.loss_gain or 0, reverse=True)

    summary_reports_list = []
    for h in harvest_data:
        summary_reports_list.append({
            "report_id": h.id,
            "batch_name": h.batch_name,
            "age": h.age,
            "initial_count": h.initial_count,
            "harvest_count": h.harvest_count,
            "mortality_pct": h.mortality_pct,
            "start_date": h.start_date.strftime('%b %d, %Y') if h.start_date else '—',
            "harvest_date": h.end_date.strftime('%b %d, %Y') if h.end_date else '—',
            "adg": h.adg,
            "fcr": h.fcr,
            "lw": h.lw,
            "expenses": h.expenses,
            "season": h.season,
            "chick_booster": h.chick_booster,
            "grower_pellets": h.grower_pellets,
            "finisher_pellets": h.finisher_pellets,
            "vaccine_day_12": h.vaccine_day_12,
            "vaccine_day_16": h.vaccine_day_16,
            "medicines": h.medicines,
            "loss_gain": h.loss_gain,
            "remarks": h.remarks,
        })

    today_prices = (MarketPrice.query
                    .filter_by(user_id=session["user_id"], record_date=date.today())
                    .order_by(MarketPrice.price_id.desc()).all())
    latest_owner_price = today_prices[0] if today_prices else None

    return render_template_string(TEMPLATE_OWNER,
        full_name=session["full_name"],
        today_str=date.today().isoformat(),
        current_year=date.today().year,
        expense_summary=get_expense_summary(),
        users=User.query.order_by(User.user_id).all(),
        flocks=all_flocks,
        active_flocks=active_flocks,
        total_birds=sum(f.current_bird_count for f in active_flocks),
        totals=totals,
        avg_market=avg_market,
        live_market=get_live_market_data(),
        today_prices=today_prices,
        latest_owner_price=latest_owner_price,
        harvest_chart_data=harvest_data_sorted,
        all_harvest_data=harvest_data_sorted,
        summary_reports_list=summary_reports_list,
        sales_forecast=get_monthly_sales_forecast(),
        flock_analytics=get_flock_analytics(active_flocks),
        profit_loss=get_profit_loss_summary(),
        harvest_profit_summary=get_harvest_profit_summary(),
        current_sort=sort,
    )

@bp.route("/manager")
@login_required
@role_required("Manager", "Owner")
def manager_dashboard():
    flocks = FlockBatch.query.order_by(FlockBatch.batch_id.desc()).all()
    active_flocks = FlockBatch.query.filter_by(flock_status='Active').all()
    totals = get_flock_totals(active_flocks)
    expense_summary = get_expense_summary()
    pending_submissions = (DailyRecordSubmission.query.filter_by(status='Pending')
                            .order_by(DailyRecordSubmission.submitted_at.asc()).all())

    month_param = request.args.get("month")
    sel_year, sel_month = None, None
    if month_param:
        try:
            sel_year, sel_month = (int(p) for p in month_param.split("-"))
        except ValueError:
            sel_year, sel_month = None, None
    category_spending = get_category_spending(sel_year, sel_month)

    # Group other expenses by category for dynamic cards
    other_expenses_all = OtherExpense.query.order_by(OtherExpense.expense_id.desc()).all()
    other_by_category = {}
    for e in other_expenses_all:
        cat = e.category.category_name if e.category else "Uncategorized"
        other_by_category.setdefault(cat, []).append(e)

    # Vaccine and feed expenses
    vaccine_expenses = VaccineExpense.query.order_by(VaccineExpense.expense_id.desc()).all()
    feed_expenses = FeedExpense.query.order_by(FeedExpense.expense_id.desc()).all()

    return render_template_string(TEMPLATE_MANAGER,
        full_name=session["full_name"],
        today_str=date.today().isoformat(),
        flocks=flocks,
        active_flocks=active_flocks,
        totals=totals,
        vaccines=Vaccine.query.order_by(Vaccine.vaccine_name).all(),
        vaccination_records=VaccinationRecord.query.order_by(VaccinationRecord.scheduled_date.desc()).all(),
        vitamins=Vitamin.query.order_by(Vitamin.vitamin_name).all(),
        vitamin_schedules=VitaminSchedule.query.order_by(VitaminSchedule.scheduled_date.desc()).all(),
        feed_records=FeedRecord.query.order_by(FeedRecord.feed_category, FeedRecord.feed_name).all(),
        medication_schedules=MedicationSchedule.query.order_by(MedicationSchedule.scheduled_date.desc()).all(),
        upcoming_schedule=get_upcoming_schedule(7),
        flock_analytics=get_flock_analytics(active_flocks),
        sales_forecast=get_monthly_sales_forecast(),
        day12_vaccine=get_day12_vaccine(),
        day16_vaccine=get_day16_vaccine(),
        medication_count=MedicationSchedule.query.filter_by(status='Scheduled').count(),
        expense_categories=ExpenseCategory.query.all(),
        water_expenses=WaterExpense.query.order_by(WaterExpense.expense_id.desc()).all(),
        electricity_expenses=ElectricityExpense.query.order_by(ElectricityExpense.expense_id.desc()).all(),
        lpg_expenses=LpgExpense.query.order_by(LpgExpense.expense_id.desc()).all(),
        labor_expenses=LaborExpense.query.order_by(LaborExpense.expense_id.desc()).all(),
        other_expenses=other_expenses_all,
        other_by_category=other_by_category,
        vaccine_expenses=vaccine_expenses,
        feed_expenses=feed_expenses,
        expense_summary=expense_summary,
        profit_loss=get_profit_loss_summary(),
        harvest_sales=HarvestSale.query.order_by(HarvestSale.sale_date.desc(), HarvestSale.sale_id.desc()).all(),
        pending_submissions=pending_submissions,
        category_spending=category_spending,
        harvest_history=HarvestHistory.query.order_by(HarvestHistory.end_date.desc()).all()
    )

@bp.route("/worker")
@login_required
def worker_dashboard():
    active_batch = get_active_batch()
    my_submissions = (DailyRecordSubmission.query.filter_by(user_id=session["user_id"])
                       .order_by(DailyRecordSubmission.submitted_at.desc()).limit(15).all())
    return render_template_string(TEMPLATE_WORKER,
        full_name=session["full_name"],
        active_batch=active_batch,
        my_records=my_submissions,
        feed_records=FeedRecord.query.order_by(FeedRecord.feed_category, FeedRecord.feed_name).all(),
        today_tasks=get_today_tasks(),
        today_date=date.today().strftime('%Y-%m-%d')
    )

# ─── Owner-only Account Management ──────────────────────────────────────────

@bp.route("/owner/user/add", methods=["POST"])
@login_required
@role_required("Owner")
def add_user():
    if User.query.filter_by(username=request.form["username"]).first():
        flash("That username is already taken.")
        return redirect(url_for("main.owner_dashboard"))

    role = request.form["role"]
    if role not in ("Manager", "Worker"):
        flash("Only Manager or Worker accounts can be created here.")
        return redirect(url_for("main.owner_dashboard"))

    phone = (request.form.get("phone_num") or "").strip()
    if not re.fullmatch(r"09\d{9}", phone):
        flash("Phone number must be 11 digits and start with 09 (e.g. 09171234567).")
        return redirect(url_for("main.owner_dashboard"))

    u = User(
        first_name=request.form["first_name"],
        middle_name=request.form.get("middle_name") or None,
        last_name=request.form["last_name"],
        phone_num=phone,
        bday=date(2000, 1, 1),
        username=request.form["username"],
        password_hash=generate_password_hash(request.form["password"]),
        role=role,
        is_active=True,
    )
    db.session.add(u)
    db.session.commit()
    flash(f"Account for {u.full_name} created.")
    return redirect(url_for("main.owner_dashboard"))

@bp.route("/owner/user/edit/<int:id>", methods=["POST"])
@login_required
@role_required("Owner")
def edit_user(id):
    u = User.query.get_or_404(id)
    u.first_name = request.form.get("first_name", u.first_name).strip()
    u.middle_name = (request.form.get("middle_name") or "").strip() or None
    u.last_name = request.form.get("last_name", u.last_name).strip()

    phone = (request.form.get("phone_num") or "").strip()
    if phone and not re.fullmatch(r"09\d{9}", phone):
        flash("Phone number must be 11 digits and start with 09.")
        return redirect(url_for("main.owner_dashboard"))
    u.phone_num = phone or None

    db.session.commit()
    flash(f"Updated {u.full_name}.")
    return redirect(url_for("main.owner_dashboard"))

@bp.route("/owner/user/deactivate/<int:id>", methods=["POST"])
@login_required
@role_required("Owner")
def deactivate_user(id):
    u = User.query.get_or_404(id)
    if u.username == "owner":
        flash("Cannot deactivate the default owner account.")
        return redirect(url_for("main.owner_dashboard"))
    u.is_active = not u.is_active
    db.session.commit()
    flash(f"{'Activated' if u.is_active else 'Deactivated'} {u.full_name}.")
    return redirect(url_for("main.owner_dashboard"))

@bp.route("/owner/user/reset-password/<int:id>", methods=["POST"])
@login_required
@role_required("Owner")
def reset_user_password(id):
    u = User.query.get_or_404(id)
    new_password = request.form.get("new_password")
    if new_password and len(new_password) >= 6:
        u.password_hash = generate_password_hash(new_password)
        db.session.commit()
        flash(f"Password reset for {u.full_name}.")
    else:
        flash("Password must be at least 6 characters.")
    return redirect(url_for("main.owner_dashboard"))

@bp.route("/owner/user/delete/<int:id>", methods=["POST"])
@login_required
@role_required("Owner")
def delete_user(id):
    u = User.query.get_or_404(id)
    if u.username != "owner":
        db.session.delete(u)
        db.session.commit()
        flash("User removed.")
    else:
        flash("Cannot delete the default owner account.")
    return redirect(url_for("main.owner_dashboard"))

# ─── Flock Management ───────────────────────────────────────────────────────

@bp.route("/owner/flock/add", methods=["POST"])
@login_required
@role_required("Owner")
def add_flock():
    existing_active = FlockBatch.query.filter_by(flock_status="Active").first()
    if existing_active:
        flash(f"'{existing_active.batch_name}' is still Active. Harvest it first before starting a new batch.")
        return redirect(url_for("main.owner_dashboard"))

    count = int(request.form["initial_bird_count"])
    start_str = (request.form.get("start_date") or "").strip()
    target_str = (request.form.get("target_harvest_date") or "").strip()
    season = (request.form.get("season") or "").strip()

    if not start_str or not target_str:
        flash("Date of Arrival and Target Harvest Date are both required.")
        return redirect(url_for("main.owner_dashboard"))

    try:
        start_date = datetime.strptime(start_str, "%Y-%m-%d").date()
        target_date = datetime.strptime(target_str, "%Y-%m-%d").date()
    except ValueError:
        flash("Invalid date format.")
        return redirect(url_for("main.owner_dashboard"))

    if target_date <= start_date:
        flash("Target Harvest Date must be after the Date of Arrival.")
        return redirect(url_for("main.owner_dashboard"))

    if season not in ("Dry", "Wet"):
        flash("Please select a Season of Arrival (Dry or Wet).")
        return redirect(url_for("main.owner_dashboard"))

    custom_suffix = request.form.get("batch_suffix") or ""

    f = FlockBatch(
        user_id=session["user_id"],
        batch_name=generate_batch_name(custom_suffix),
        initial_bird_count=count,
        current_bird_count=count,
        start_date=start_date,
        target_harvest_date=target_date,
        season=season,
    )
    db.session.add(f)
    db.session.commit()
    flash(f"Flock '{f.batch_name}' created.")
    return redirect(url_for("main.owner_dashboard"))

@bp.route("/owner/flock/edit/<int:id>", methods=["POST"])
@login_required
@role_required("Owner")
def edit_flock(id):
    f = FlockBatch.query.get_or_404(id)
    if f.flock_status == "Harvested":
        flash("This batch is Harvested and can no longer be edited.")
        return redirect(url_for("main.owner_dashboard"))

    new_status = request.form.get("flock_status", f.flock_status)

    if new_status == "Harvested" and not f.has_data:
        flash("Cannot mark this batch as Harvested — it has no recorded data yet "
              "(no daily submissions, growth, feed, or sales).")
        return redirect(url_for("main.owner_dashboard"))

    if new_status == "Active" and f.flock_status != "Active":
        other_active = FlockBatch.query.filter(
            FlockBatch.flock_status == "Active", FlockBatch.batch_id != f.batch_id
        ).first()
        if other_active:
            flash(f"'{other_active.batch_name}' is already Active. Mark it Harvested first.")
            return redirect(url_for("main.owner_dashboard"))

    f.batch_name = request.form["batch_name"]
    f.flock_status = new_status

    db.session.commit()
    flash(f"Flock '{f.batch_name}' updated.")
    return redirect(url_for("main.owner_dashboard"))

@bp.route("/manager/flock/harvest/<int:id>", methods=["POST"])
@login_required
@role_required("Manager", "Owner")
def harvest_flock(id):
    """Harvest is now restricted to Manager (and Owner as fallback)."""
    f = FlockBatch.query.get_or_404(id)
    if f.flock_status != "Active":
        flash("This batch is not active.")
        return redirect_dashboard()

    if not f.has_data:
        flash("Cannot harvest this batch — it has no recorded data yet. "
              "Daily submissions, growth, feed, or sales must exist first.")
        return redirect_dashboard()

    snap = get_batch_snapshot(f)

    batch_expenses = 0.0
    batch_expenses += db.session.query(func.sum(WaterExpense.water_expense_amount)).filter_by(batch_id=f.batch_id).scalar() or 0.0
    batch_expenses += db.session.query(func.sum(ElectricityExpense.electricity_expense_amount)).filter_by(batch_id=f.batch_id).scalar() or 0.0
    batch_expenses += db.session.query(func.sum(LpgExpense.lpg_expense_amount)).filter_by(batch_id=f.batch_id).scalar() or 0.0
    batch_expenses += db.session.query(func.sum(LaborExpense.labor_expense_amount)).filter_by(batch_id=f.batch_id).scalar() or 0.0
    batch_expenses += db.session.query(func.sum(OtherExpense.other_expense_amount)).filter_by(batch_id=f.batch_id).scalar() or 0.0
    batch_expenses += db.session.query(func.sum(VaccineExpense.vaccine_expense_amount)).filter_by(batch_id=f.batch_id).scalar() or 0.0
    batch_expenses += db.session.query(func.sum(FeedExpense.feed_expense_amount)).filter_by(batch_id=f.batch_id).scalar() or 0.0

    batch_revenue = db.session.query(func.sum(HarvestSale.total_amount)).filter_by(batch_id=f.batch_id).scalar() or 0.0

    day12_vax = VaccinationRecord.query.filter_by(batch_id=f.batch_id).first()
    day16_vax = VaccinationRecord.query.filter_by(batch_id=f.batch_id).offset(1).first()

    if f.season in ("Dry", "Wet"):
        season = f.season
    else:
        month = f.start_date.month if f.start_date else 1
        if month in [12, 1, 2]:
            season = "Wet"
        elif month in [3, 4, 5]:
            season = "Dry"
        else:
            season = "Wet"

    harvest = HarvestHistory(
        batch_name=f.batch_name,
        start_date=f.start_date,
        end_date=date.today(),
        age=snap["age_days"],
        initial_count=f.initial_bird_count,
        harvest_count=f.current_bird_count,
        mortality_pct=f.mortality_percentage,
        total_deaths=f.mortality_count,
        culled=0,
        adg=snap["adg_value"],
        fcr=snap["fcr_value"],
        lw=snap["latest_weight_g"],
        expenses=batch_expenses,
        season=season,
        vaccine_day_12=day12_vax.vaccine.vaccine_name if day12_vax and day12_vax.vaccine else None,
        vaccine_day_16=day16_vax.vaccine.vaccine_name if day16_vax and day16_vax.vaccine else None,
        budget_allocated=f.budget_allocated,
        loss_gain=round(batch_revenue - batch_expenses, 2),
        remarks="Batch harvested and archived."
    )
    db.session.add(harvest)

    f.flock_status = "Harvested"
    db.session.commit()
    flash(f"Batch '{f.batch_name}' has been harvested and archived.")
    return redirect_dashboard()

@bp.route("/owner/flock/delete/<int:id>", methods=["POST"])
@login_required
@role_required("Owner")
def delete_flock(id):
    f = FlockBatch.query.get_or_404(id)
    db.session.delete(f)
    db.session.commit()
    flash("Flock deleted.")
    return redirect(url_for("main.owner_dashboard"))

# ─── Market Prices ──────────────────────────────────────────────────────────

@bp.route("/owner/market-price/add", methods=["POST"])
@login_required
@role_required("Owner")
def add_market_price():
    date_str = request.form.get("record_date")
    if date_str:
        try:
            rec_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            flash("Invalid date.")
            return redirect(url_for("main.owner_dashboard"))
        if rec_date > date.today():
            flash("Record date cannot be later than today.")
            return redirect(url_for("main.owner_dashboard"))
    else:
        rec_date = date.today()

    mp = MarketPrice(
        user_id=session["user_id"],
        record_date=rec_date,
        price_per_kg=float(request.form["price_per_kg"]),
        location=request.form.get("location"),
    )
    db.session.add(mp)
    db.session.commit()
    flash("Price recorded.")
    return redirect(url_for("main.owner_dashboard"))

# ─── Expense Tracking ──────────────────────────────────────────────────────

@bp.route("/owner/expense-category/add", methods=["POST"])
@login_required
@role_required("Owner", "Manager")
def add_expense_category():
    name = request.form.get("category_name", "").strip()
    if not name:
        flash("Category name is required.")
        return redirect_dashboard()
    existing = ExpenseCategory.query.filter(func.lower(ExpenseCategory.category_name) == name.lower()).first()
    if existing:
        flash(f"Category '{name}' already exists.")
        return redirect_dashboard()
    c = ExpenseCategory(user_id=session["user_id"], category_name=name)
    db.session.add(c)
    db.session.commit()
    flash(f"Category '{c.category_name}' added.")
    return redirect_dashboard()

@bp.route("/owner/expense-category/delete/<int:id>", methods=["POST"])
@login_required
@role_required("Owner", "Manager")
def delete_expense_category(id):
    c = ExpenseCategory.query.get_or_404(id)
    db.session.delete(c)
    db.session.commit()
    flash("Category removed.")
    return redirect_dashboard()

@bp.route("/owner/expense/water/add", methods=["POST"])
@login_required
@role_required("Owner", "Manager")
def add_water_expense():
    cat = get_or_create_category("Water")
    active = get_active_batch()
    e = WaterExpense(
        expense_category_id=cat.expense_category_id,
        batch_id=active.batch_id if active else None,
        water_expense_amount=float(request.form["amount"]),
        water_expense_status=request.form.get("status", "Pending"),
        expense_date=parse_expense_date(request.form)
    )
    db.session.add(e)
    db.session.commit()
    flash("Water expense logged.")
    return redirect_dashboard()

@bp.route("/owner/expense/water/toggle/<int:id>", methods=["POST"])
@login_required
@role_required("Owner", "Manager")
def toggle_water_expense(id):
    e = WaterExpense.query.get_or_404(id)
    e.water_expense_status = "Paid" if e.water_expense_status != "Paid" else "Pending"
    db.session.commit()
    return redirect_dashboard()

@bp.route("/owner/expense/water/delete/<int:id>", methods=["POST"])
@login_required
@role_required("Owner", "Manager")
def delete_water_expense(id):
    e = WaterExpense.query.get_or_404(id)
    db.session.delete(e)
    db.session.commit()
    return redirect_dashboard()

@bp.route("/owner/expense/electricity/add", methods=["POST"])
@login_required
@role_required("Owner", "Manager")
def add_electricity_expense():
    cat = get_or_create_category("Electricity")
    active = get_active_batch()
    e = ElectricityExpense(
        expense_category_id=cat.expense_category_id,
        batch_id=active.batch_id if active else None,
        electricity_expense_amount=float(request.form["amount"]),
        electricity_expense_status=request.form.get("status", "Pending"),
        expense_date=parse_expense_date(request.form)
    )
    db.session.add(e)
    db.session.commit()
    flash("Electricity expense logged.")
    return redirect_dashboard()

@bp.route("/owner/expense/electricity/toggle/<int:id>", methods=["POST"])
@login_required
@role_required("Owner", "Manager")
def toggle_electricity_expense(id):
    e = ElectricityExpense.query.get_or_404(id)
    e.electricity_expense_status = "Paid" if e.electricity_expense_status != "Paid" else "Pending"
    db.session.commit()
    return redirect_dashboard()

@bp.route("/owner/expense/electricity/delete/<int:id>", methods=["POST"])
@login_required
@role_required("Owner", "Manager")
def delete_electricity_expense(id):
    e = ElectricityExpense.query.get_or_404(id)
    db.session.delete(e)
    db.session.commit()
    return redirect_dashboard()

@bp.route("/owner/expense/lpg/add", methods=["POST"])
@login_required
@role_required("Owner", "Manager")
def add_lpg_expense():
    cat = get_or_create_category("LPG")
    active = get_active_batch()
    e = LpgExpense(
        expense_category_id=cat.expense_category_id,
        batch_id=active.batch_id if active else None,
        lpg_expense_amount=float(request.form["amount"]),
        lpg_provider=request.form.get("lpg_provider"),
        lpg_expense_status=request.form.get("status", "Pending"),
        expense_date=parse_expense_date(request.form)
    )
    db.session.add(e)
    db.session.commit()
    flash("LPG expense logged.")
    return redirect_dashboard()

@bp.route("/owner/expense/lpg/toggle/<int:id>", methods=["POST"])
@login_required
@role_required("Owner", "Manager")
def toggle_lpg_expense(id):
    e = LpgExpense.query.get_or_404(id)
    e.lpg_expense_status = "Paid" if e.lpg_expense_status != "Paid" else "Pending"
    db.session.commit()
    return redirect_dashboard()

@bp.route("/owner/expense/lpg/delete/<int:id>", methods=["POST"])
@login_required
@role_required("Owner", "Manager")
def delete_lpg_expense(id):
    e = LpgExpense.query.get_or_404(id)
    db.session.delete(e)
    db.session.commit()
    return redirect_dashboard()

@bp.route("/owner/expense/labor/add", methods=["POST"])
@login_required
@role_required("Owner", "Manager")
def add_labor_expense():
    cat = get_or_create_category("Labor")
    active = get_active_batch()
    e = LaborExpense(
        expense_category_id=cat.expense_category_id,
        batch_id=active.batch_id if active else None,
        labor_expense_amount=float(request.form["amount"]),
        labor_expense_status=request.form.get("status", "Pending"),
        expense_date=parse_expense_date(request.form)
    )
    db.session.add(e)
    db.session.commit()
    flash("Labor expense logged.")
    return redirect_dashboard()

@bp.route("/owner/expense/labor/toggle/<int:id>", methods=["POST"])
@login_required
@role_required("Owner", "Manager")
def toggle_labor_expense(id):
    e = LaborExpense.query.get_or_404(id)
    e.labor_expense_status = "Paid" if e.labor_expense_status != "Paid" else "Pending"
    db.session.commit()
    return redirect_dashboard()

@bp.route("/owner/expense/labor/delete/<int:id>", methods=["POST"])
@login_required
@role_required("Owner", "Manager")
def delete_labor_expense(id):
    e = LaborExpense.query.get_or_404(id)
    db.session.delete(e)
    db.session.commit()
    return redirect_dashboard()

@bp.route("/owner/expense/other/add", methods=["POST"])
@login_required
@role_required("Owner", "Manager")
def add_other_expense():
    active = get_active_batch()
    e = OtherExpense(
        user_id=session["user_id"],
        expense_category_id=int(request.form["expense_category_id"]),
        batch_id=active.batch_id if active else None,
        other_expense_amount=float(request.form["amount"]),
        other_expense_status=request.form.get("status", "Pending"),
        expense_date=parse_expense_date(request.form)
    )
    db.session.add(e)
    db.session.commit()
    flash("Expense logged.")
    return redirect_dashboard()

@bp.route("/owner/expense/other/toggle/<int:id>", methods=["POST"])
@login_required
@role_required("Owner", "Manager")
def toggle_other_expense(id):
    e = OtherExpense.query.get_or_404(id)
    e.other_expense_status = "Paid" if e.other_expense_status != "Paid" else "Pending"
    db.session.commit()
    return redirect_dashboard()

@bp.route("/owner/expense/other/delete/<int:id>", methods=["POST"])
@login_required
@role_required("Owner", "Manager")
def delete_other_expense(id):
    e = OtherExpense.query.get_or_404(id)
    db.session.delete(e)
    db.session.commit()
    return redirect_dashboard()

# ─── Harvest Sales ───────────────────────────────────────────────────────────

@bp.route("/manager/sale/add", methods=["POST"])
@login_required
@role_required("Owner", "Manager")
def add_harvest_sale():
    kg_sold = float(request.form["kg_sold"])
    price_per_kg = float(request.form["price_per_kg"])
    sale_date_str = request.form.get("sale_date")
    s = HarvestSale(
        batch_id=int(request.form["batch_id"]),
        user_id=session["user_id"],
        sale_date=datetime.strptime(sale_date_str, "%Y-%m-%d").date() if sale_date_str else date.today(),
        kg_sold=kg_sold,
        price_per_kg=price_per_kg,
        total_amount=round(kg_sold * price_per_kg, 2),
        buyer=request.form.get("buyer") or None,
        remarks=request.form.get("remarks") or None
    )
    db.session.add(s)
    db.session.commit()
    flash("Harvest sale logged.")
    return redirect_dashboard()

@bp.route("/manager/sale/delete/<int:id>", methods=["POST"])
@login_required
@role_required("Owner", "Manager")
def delete_harvest_sale(id):
    s = HarvestSale.query.get_or_404(id)
    db.session.delete(s)
    db.session.commit()
    flash("Harvest sale removed.")
    return redirect_dashboard()

# ─── Vaccine Management ──────────────────────────────────────────────────────

@bp.route("/manager/vaccine/add", methods=["POST"])
@login_required
@role_required("Manager", "Owner")
def add_vaccine():
    exp_str = request.form.get("vaccine_exp_date")
    v = Vaccine(
        user_id=session["user_id"],
        vaccine_name=request.form["vaccine_name"],
        vaccine_type=request.form.get("vaccine_type"),
        vaccine_exp_date=datetime.strptime(exp_str, "%Y-%m-%d").date() if exp_str else None,
        milliliters_per_bottle=float(request.form.get("milliliters_per_bottle", 0) or 0),
        remaining_quantity=float(request.form.get("remaining_quantity", 0) or 0),
        cost_per_bottle=float(request.form.get("cost_per_bottle", 0) or 0),
    )
    db.session.add(v)
    db.session.commit()
    flash(f"Vaccine '{v.vaccine_name}' added.")
    return redirect(url_for("main.manager_dashboard"))

@bp.route("/manager/vaccine/edit/<int:id>", methods=["POST"])
@login_required
@role_required("Manager", "Owner")
def edit_vaccine(id):
    v = Vaccine.query.get_or_404(id)
    exp_str = request.form.get("vaccine_exp_date")
    v.vaccine_name = request.form["vaccine_name"]
    v.vaccine_type = request.form.get("vaccine_type")
    v.vaccine_exp_date = datetime.strptime(exp_str, "%Y-%m-%d").date() if exp_str else None
    v.milliliters_per_bottle = float(request.form.get("milliliters_per_bottle", 0) or 0)
    v.remaining_quantity = float(request.form.get("remaining_quantity", 0) or 0)
    v.cost_per_bottle = float(request.form.get("cost_per_bottle", 0) or 0)
    db.session.commit()
    flash("Vaccine updated.")
    return redirect(url_for("main.manager_dashboard"))

@bp.route("/manager/vaccine/delete/<int:id>", methods=["POST"])
@login_required
@role_required("Manager", "Owner")
def delete_vaccine(id):
    v = Vaccine.query.get_or_404(id)
    db.session.delete(v)
    db.session.commit()
    flash("Vaccine removed.")
    return redirect(url_for("main.manager_dashboard"))

@bp.route("/manager/vaccination/schedule", methods=["POST"])
@login_required
@role_required("Manager", "Owner")
def schedule_vaccination():
    scheduled_dt = datetime.strptime(request.form["scheduled_date"], "%Y-%m-%dT%H:%M")
    v = VaccinationRecord(
        batch_id=int(request.form["batch_id"]),
        vaccine_id=int(request.form["vaccine_id"]),
        user_id=session["user_id"],
        dose_per_bird=float(request.form.get("dose_per_bird", 0) or 0),
        scheduled_date=scheduled_dt,
        status="Scheduled"
    )
    db.session.add(v)
    db.session.commit()
    flash("Vaccination scheduled.")
    return redirect(url_for("main.manager_dashboard"))

@bp.route("/manager/vaccination/administer/<int:id>", methods=["POST"])
@login_required
@role_required("Manager", "Owner")
def administer_vaccination(id):
    v = VaccinationRecord.query.get_or_404(id)
    v.status = "Administered"
    v.administered_by = session["full_name"]
    if v.vaccine and v.vaccine.milliliters_per_bottle and v.batch:
        total_ml_needed = v.dose_per_bird * v.batch.current_bird_count
        bottles_used = total_ml_needed / v.vaccine.milliliters_per_bottle
        v.vaccine.remaining_quantity = max(0.0, round(v.vaccine.remaining_quantity - bottles_used, 2))
        # Auto-log vaccine expense
        cost = round(bottles_used * (v.vaccine.cost_per_bottle or 0), 2)
        if cost > 0:
            db.session.add(VaccineExpense(
                vaccine_id=v.vaccine.vaccine_id,
                batch_id=v.batch_id,
                vaccine_expense_amount=cost,
                vaccine_expense_status="Paid",
                expense_date=date.today(),
                description=f"{v.vaccine.vaccine_name} — {round(bottles_used, 2)} bottle(s)"
            ))
    db.session.commit()
    flash("Vaccination marked as administered.")
    return redirect(url_for("main.manager_dashboard"))

@bp.route("/manager/vaccination/delete/<int:id>", methods=["POST"])
@login_required
@role_required("Manager", "Owner")
def delete_vaccination(id):
    v = VaccinationRecord.query.get_or_404(id)
    db.session.delete(v)
    db.session.commit()
    return redirect(url_for("main.manager_dashboard"))

# ─── Vitamin Management ─────────────────────────────────────────────────────

@bp.route("/manager/vitamin/add", methods=["POST"])
@login_required
@role_required("Manager", "Owner")
def add_vitamin():
    exp_str = request.form.get("vitamin_exp_date")
    v = Vitamin(
        user_id=session["user_id"],
        vitamin_name=request.form["vitamin_name"],
        vitamin_type=request.form.get("vitamin_type"),
        vitamin_exp_date=datetime.strptime(exp_str, "%Y-%m-%d").date() if exp_str else None,
        quantity=float(request.form.get("quantity", 0) or 0),
        unit=request.form.get("unit"),
        cost_per_unit=float(request.form.get("cost_per_unit", 0) or 0),
    )
    db.session.add(v)
    db.session.commit()
    flash(f"Vitamin '{v.vitamin_name}' added.")
    return redirect(url_for("main.manager_dashboard"))

@bp.route("/manager/vitamin/edit/<int:id>", methods=["POST"])
@login_required
@role_required("Manager", "Owner")
def edit_vitamin(id):
    v = Vitamin.query.get_or_404(id)
    exp_str = request.form.get("vitamin_exp_date")
    v.vitamin_name = request.form["vitamin_name"]
    v.vitamin_type = request.form.get("vitamin_type")
    v.vitamin_exp_date = datetime.strptime(exp_str, "%Y-%m-%d").date() if exp_str else None
    v.quantity = float(request.form.get("quantity", 0) or 0)
    v.unit = request.form.get("unit")
    v.cost_per_unit = float(request.form.get("cost_per_unit", 0) or 0)
    db.session.commit()
    flash("Vitamin updated.")
    return redirect(url_for("main.manager_dashboard"))

@bp.route("/manager/vitamin/delete/<int:id>", methods=["POST"])
@login_required
@role_required("Manager", "Owner")
def delete_vitamin(id):
    v = Vitamin.query.get_or_404(id)
    db.session.delete(v)
    db.session.commit()
    flash("Vitamin removed.")
    return redirect(url_for("main.manager_dashboard"))

@bp.route("/manager/vitamin/schedule", methods=["POST"])
@login_required
@role_required("Manager", "Owner")
def schedule_vitamin():
    scheduled_dt = datetime.utcnow() + timedelta(days=int(request.form["day_given"]))
    v = VitaminSchedule(
        batch_id=int(request.form["batch_id"]),
        vitamin_id=int(request.form["vitamin_id"]),
        user_id=session["user_id"],
        day_given=int(request.form["day_given"]),
        dosage=request.form.get("dosage"),
        scheduled_date=scheduled_dt,
        status="Scheduled"
    )
    db.session.add(v)
    db.session.commit()
    flash("Vitamin scheduled.")
    return redirect(url_for("main.manager_dashboard"))

@bp.route("/manager/vitamin/administer/<int:id>", methods=["POST"])
@login_required
@role_required("Manager", "Owner")
def administer_vitamin(id):
    v = VitaminSchedule.query.get_or_404(id)
    v.status = "Administered"
    v.administered_by = session["full_name"]
    db.session.commit()
    flash("Vitamin marked as administered.")
    return redirect(url_for("main.manager_dashboard"))

@bp.route("/manager/vitamin/delete/<int:id>", methods=["POST"])
@login_required
@role_required("Manager", "Owner")
def delete_vitamin_schedule(id):
    v = VitaminSchedule.query.get_or_404(id)
    db.session.delete(v)
    db.session.commit()
    return redirect(url_for("main.manager_dashboard"))

# ─── Medicine Management ────────────────────────────────────────────────────

@bp.route("/manager/medicine/schedule", methods=["POST"])
@login_required
@role_required("Manager", "Owner")
def schedule_medicine():
    scheduled_str = request.form.get("scheduled_date")
    try:
        sched_date = datetime.strptime(scheduled_str, "%Y-%m-%d") if scheduled_str else datetime.utcnow()
    except ValueError:
        sched_date = datetime.utcnow()

    m = MedicationSchedule(
        batch_id=int(request.form["batch_id"]),
        user_id=session["user_id"],
        item_name=request.form["item_name"],
        item_type="Medicine",
        dosage=request.form.get("dosage"),
        scheduled_date=sched_date,
        status="Scheduled",
        notes=request.form.get("notes"),
    )
    db.session.add(m)
    db.session.commit()
    flash("Medicine scheduled.")
    return redirect(url_for("main.manager_dashboard"))

@bp.route("/manager/medicine/administer/<int:id>", methods=["POST"])
@login_required
@role_required("Manager", "Owner")
def administer_medicine(id):
    m = MedicationSchedule.query.get_or_404(id)
    m.status = "Administered"
    m.administered_by = session["full_name"]
    db.session.commit()
    flash("Medicine marked as administered.")
    return redirect(url_for("main.manager_dashboard"))

@bp.route("/manager/medicine/delete/<int:id>", methods=["POST"])
@login_required
@role_required("Manager", "Owner")
def delete_medicine_schedule(id):
    m = MedicationSchedule.query.get_or_404(id)
    db.session.delete(m)
    db.session.commit()
    return redirect(url_for("main.manager_dashboard"))

# ─── Feed Management ────────────────────────────────────────────────────────

@bp.route("/manager/feed/add", methods=["POST"])
@login_required
@role_required("Manager", "Owner")
def add_feed_record():
    exp_str = request.form.get("expiration_date")
    f = FeedRecord(
        user_id=session["user_id"],
        feed_name=request.form["feed_name"],
        feed_category=request.form["feed_category"],
        expiration_date=datetime.strptime(exp_str, "%Y-%m-%d").date() if exp_str else None,
        cost_per_kg=float(request.form.get("cost_per_kg", 0) or 0),
        remaining_quantity=float(request.form.get("remaining_quantity", 0) or 0),
    )
    for field in FEED_NUTRIENT_FIELDS:
        setattr(f, field, float(request.form.get(field, 0) or 0))
    db.session.add(f)
    db.session.commit()
    flash(f"Feed '{f.feed_name}' added.")
    return redirect(url_for("main.manager_dashboard"))

@bp.route("/manager/feed/edit/<int:id>", methods=["POST"])
@login_required
@role_required("Manager", "Owner")
def edit_feed_record(id):
    f = FeedRecord.query.get_or_404(id)
    exp_str = request.form.get("expiration_date")
    f.feed_name = request.form["feed_name"]
    f.feed_category = request.form["feed_category"]
    f.expiration_date = datetime.strptime(exp_str, "%Y-%m-%d").date() if exp_str else None
    f.cost_per_kg = float(request.form.get("cost_per_kg", 0) or 0)
    f.remaining_quantity = float(request.form.get("remaining_quantity", 0) or 0)
    for field in FEED_NUTRIENT_FIELDS:
        setattr(f, field, float(request.form.get(field, 0) or 0))
    db.session.commit()
    flash("Feed updated.")
    return redirect(url_for("main.manager_dashboard"))

@bp.route("/manager/feed/delete/<int:id>", methods=["POST"])
@login_required
@role_required("Manager", "Owner")
def delete_feed_record(id):
    f = FeedRecord.query.get_or_404(id)
    db.session.delete(f)
    db.session.commit()
    return redirect(url_for("main.manager_dashboard"))

# ─── Worker Daily Submission ─────────────────────────────────────────────────

@bp.route("/worker/record/add", methods=["POST"])
@login_required
def worker_add_record():
    active = get_active_batch()
    if not active:
        flash("No active flock batch to record against.")
        return redirect(url_for("main.worker_dashboard"))

    batch = active
    record_date = datetime.strptime(request.form["record_date"], "%Y-%m-%d").date()
    feed_record_id = request.form.get("feed_record_id")

    s = DailyRecordSubmission(
        batch_id=batch.batch_id,
        user_id=session["user_id"],
        record_date=record_date,
        avg_weight_g=float(request.form.get("avg_weight", 0) or 0),
        mortality=int(request.form.get("mortality", 0) or 0),
        cull=int(request.form.get("cull", 0) or 0),
        cause=request.form.get("cause"),
        feed_kg=float(request.form.get("feed_consumed", 0) or 0),
        feed_record_id=int(feed_record_id) if feed_record_id else None,
        water_consumption=request.form.get("water_consumption"),
        abnormal_behavior=request.form.get("abnormal_behavior"),
        visible_illness=request.form.get("visible_illness"),
        remarks=request.form.get("remarks"),
        status="Pending"
    )
    db.session.add(s)
    db.session.commit()
    flash(f"Daily record for {batch.batch_name} submitted — waiting for Manager verification.")
    return redirect(url_for("main.worker_dashboard"))

@bp.route("/manager/submission/approve/<int:id>", methods=["POST"])
@login_required
@role_required("Manager", "Owner")
def approve_submission(id):
    s = DailyRecordSubmission.query.get_or_404(id)
    if s.status != "Pending":
        flash("This submission has already been reviewed.")
        return redirect_dashboard()
    record_growth_data(s.batch, s.user_id, s.record_date, s.avg_weight_g, s.feed_kg,
                        s.feed_record_id, s.mortality, s.cull, s.cause)
    s.status = "Verified"
    s.reviewed_by = session["user_id"]
    s.reviewed_at = datetime.utcnow()
    db.session.commit()
    flash(f"Record for {s.batch.batch_name} ({s.record_date.strftime('%b %d')}) verified and applied.")
    return redirect_dashboard()

@bp.route("/manager/submission/reject/<int:id>", methods=["POST"])
@login_required
@role_required("Manager", "Owner")
def reject_submission(id):
    s = DailyRecordSubmission.query.get_or_404(id)
    if s.status != "Pending":
        flash("This submission has already been reviewed.")
        return redirect_dashboard()
    s.status = "Rejected"
    s.reviewed_by = session["user_id"]
    s.reviewed_at = datetime.utcnow()
    s.review_notes = request.form.get("review_notes")
    db.session.commit()
    flash(f"Record for {s.batch.batch_name} ({s.record_date.strftime('%b %d')}) rejected.")
    return redirect_dashboard()

# ─── Performance Report ─────────────────────────────────────────────────────

@bp.route("/manager/report/add", methods=["POST"])
@login_required
@role_required("Manager", "Owner")
def add_performance_report():
    flash("Reports are generated automatically from harvest data.")
    return redirect_dashboard()

@bp.route("/report/<int:id>/print")
@login_required
def print_performance_report(id):
    h = HarvestHistory.query.get_or_404(id)
    report = {
        "batch": {"batch_name": h.batch_name, "start_date": h.start_date},
        "end_date": h.end_date.strftime('%d-%m-%Y') if h.end_date else '—',
        "age": h.age,
        "initial_count": h.initial_count,
        "harvest_count": h.harvest_count,
        "mortality_pct": h.mortality_pct,
        "total_deaths": h.total_deaths,
        "culled": h.culled,
        "adg": h.adg,
        "fcr": h.fcr,
        "lw": h.lw,
        "expenses": h.expenses,
        "season": h.season,
        "chick_booster": h.chick_booster,
        "grower_pellets": h.grower_pellets,
        "finisher_pellets": h.finisher_pellets,
        "vaccine_day_12": h.vaccine_day_12,
        "vaccine_day_16": h.vaccine_day_16,
        "medicines": h.medicines,
        "budget_allocated": h.budget_allocated,
        "loss_gain": h.loss_gain,
        "remarks": h.remarks,
        "farm_head_name": "Manager"
    }

    ALL_FIELDS = [
        "batch_name", "age", "initial_count", "harvest_count",
        "mortality_pct", "start_date", "harvest_date", "adg", "fcr", "lw",
        "expenses", "season", "chick_booster", "grower_pellets", "finisher_pellets",
        "vaccine_day_12", "vaccine_day_16", "medicines", "loss_gain", "remarks"
    ]

    fields_param = request.args.get("fields", "")
    if fields_param == "all" or not fields_param:
        selected_fields = ALL_FIELDS
    else:
        selected_fields = [f.strip() for f in fields_param.split(",") if f.strip()]
        if not selected_fields:
            selected_fields = ALL_FIELDS

    return render_template_string(
        TEMPLATE_PERFORMANCE_REPORT_PRINT,
        report=report,
        selected_fields=selected_fields
    )