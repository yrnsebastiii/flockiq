# seed_data.py
"""Run once after `python run.py` has created tables."""
import random
from datetime import date, datetime, timedelta
from run import app
from db_ext import db
from flock_models import (
    User, FlockBatch, Vaccine, VaccinationRecord, MedicationSchedule,
    Vitamin, VitaminSchedule, FeedRecord, DailyFeedRecord,
    MortalityRecord, WeightRecord, AdgCalculation, FcrCalculation,
    FlockReport, MarketPrice, ExpenseCategory,
    WaterExpense, ElectricityExpense, LpgExpense, LaborExpense,
    OtherExpense, HarvestHistory, HarvestSale, DailyRecordSubmission,
    VaccineExpense, FeedExpense,
)
from flock_routes import record_growth_data
from werkzeug.security import generate_password_hash


def get_or_create_user(**kw):
    u = User.query.filter_by(username=kw["username"]).first()
    if u:
        return u
    u = User(**kw)
    db.session.add(u)
    db.session.flush()
    return u


def seed():
    with app.app_context():
        if User.query.filter_by(role="Manager").first():
            print("Sample data already present. Skipping.")
            return
        owner = User.query.filter_by(username="owner").first()
        assert owner, "Run run.py once so the owner account exists."

        manager = get_or_create_user(
            username="manager1", password_hash=generate_password_hash("manager123"),
            role="Manager", first_name="Maria", middle_name="Santos", last_name="Reyes",
            phone_num="09171234567", email="maria.reyes@flockiq.ph",
            address="Meycauayan, Bulacan", bday=date(1990, 5, 14), is_active=True)

        workers = []
        for uname, fn, mn, ln, phone in [
            ("worker1", "Juan", "Dela", "Cruz", "09181112222"),
            ("worker2", "Pedro", "Ramos", "Lim", "09182223333"),
            ("worker3", "Ana", "Garcia", "Tan", "09183334444")]:
            workers.append(get_or_create_user(
                username=uname, password_hash=generate_password_hash("worker123"),
                role="Worker", first_name=fn, middle_name=mn, last_name=ln,
                phone_num=phone, email=f"{uname}@flockiq.ph",
                address="Meycauayan, Bulacan",
                bday=date(1998, random.randint(1, 12), random.randint(1, 28)),
                is_active=True))

        cats = {}
        for n in ["Water", "Electricity", "LPG", "Labor", "Supplies", "Miscellaneous"]:
            c = ExpenseCategory.query.filter_by(category_name=n).first()
            if not c:
                c = ExpenseCategory(user_id=owner.user_id, category_name=n)
                db.session.add(c)
            cats[n] = c
        db.session.flush()

        feeds = []
        feed_defs = [
            ("Chick Booster",   "Broiler Starter Crumble", 22.0, 5.0, 3.5, 12.0, 1.00, 0.45),
            ("Grower Pellets",  "Broiler Grower Pellet",   19.5, 5.5, 4.0, 12.0, 0.90, 0.42),
            ("Finisher Pellets","Broiler Finisher Pellet", 17.5, 6.0, 4.5, 12.0, 0.85, 0.40),
        ]
        for cat, name, cp, fat, fib, moist, ca, p in feed_defs:
            f = FeedRecord.query.filter_by(feed_name=name).first()
            if not f:
                f = FeedRecord(
                    user_id=manager.user_id, feed_name=name, feed_category=cat,
                    expiration_date=date.today() + timedelta(days=180),
                    crude_protein=cp, crude_fat=fat, crude_fiber=fib,
                    moisture=moist, calcium=ca, phosphorus=p,
                    cost_per_kg=32.0,
                    remaining_quantity=500.0,
                )
                db.session.add(f)
            feeds.append(f)
        db.session.flush()

        vaccines = []
        for name, typ, ml, stock in [
            ("Newcastle Disease (NDV)", "Live", 100.0, 12.0),
            ("Infectious Bursal (IBD)", "Live", 100.0, 10.0),
            ("Infectious Bronchitis", "Live", 100.0, 8.0)]:
            v = Vaccine.query.filter_by(vaccine_name=name).first()
            if not v:
                v = Vaccine(user_id=manager.user_id, vaccine_name=name, vaccine_type=typ,
                            vaccine_exp_date=date.today() + timedelta(days=365),
                            milliliters_per_bottle=ml, remaining_quantity=stock,
                            cost_per_bottle=450.0)
                db.session.add(v)
            vaccines.append(v)

        vitamins = []
        for name, typ, qty, unit in [
            ("Vitamin B-Complex", "Water-soluble", 5.0, "L"),
            ("Vitamin C", "Water-soluble", 3.0, "L"),
            ("Electrolyte Plus", "Water-soluble", 4.0, "L")]:
            v = Vitamin.query.filter_by(vitamin_name=name).first()
            if not v:
                v = Vitamin(user_id=manager.user_id, vitamin_name=name, vitamin_type=typ,
                            vitamin_exp_date=date.today() + timedelta(days=365),
                            quantity=qty, unit=unit, cost_per_unit=350.0)
                db.session.add(v)
            vitamins.append(v)
        db.session.flush()

        active = FlockBatch.query.filter_by(flock_status="Active").first()
        if not active:
            start = date.today() - timedelta(days=20)
            active = FlockBatch(
                user_id=owner.user_id, batch_name="Batch-2026-A",
                start_date=start,
                target_harvest_date=start + timedelta(days=35),
                initial_bird_count=5000, current_bird_count=5000,
                season="Dry",
                flock_status="Active")
            db.session.add(active)
            db.session.flush()

        harvested = []
        for i, days_ago in enumerate([120, 90, 60, 45]):
            start = date.today() - timedelta(days=days_ago + 40)
            b = FlockBatch(
                user_id=owner.user_id, batch_name=f"Batch-2025-{chr(65 + i)}",
                start_date=start, target_harvest_date=start + timedelta(days=40),
                initial_bird_count=random.randint(4000, 6000),
                current_bird_count=0,
                season=random.choice(["Dry", "Wet"]),
                flock_status="Harvested")
            b.current_bird_count = int(b.initial_bird_count * random.uniform(0.92, 0.97))
            db.session.add(b)
            harvested.append(b)
        db.session.flush()

        for v, day in zip(vaccines, [10, 14, 21]):
            sched = datetime.combine(active.start_date + timedelta(days=day), datetime.min.time()) + timedelta(hours=8)
            db.session.add(VaccinationRecord(
                batch_id=active.batch_id, vaccine_id=v.vaccine_id,
                user_id=manager.user_id, dose_per_bird=0.03,
                administered_by=manager.full_name if day <= 20 else None,
                scheduled_date=sched,
                status="Administered" if day <= 20 else "Scheduled"))
        for v, day in zip(vitamins, [5, 12, 18]):
            sched = datetime.combine(active.start_date + timedelta(days=day), datetime.min.time()) + timedelta(hours=6)
            db.session.add(VitaminSchedule(
                batch_id=active.batch_id, vitamin_id=v.vitamin_id,
                user_id=manager.user_id, day_given=day,
                dosage="2 mL / L water", scheduled_date=sched,
                status="Administered" if day <= 20 else "Scheduled",
                administered_by=manager.full_name if day <= 20 else None))
        for name, day in [("Amoxicillin", 3), ("Tylosin", 17)]:
            sched = datetime.combine(active.start_date + timedelta(days=day), datetime.min.time()) + timedelta(hours=7)
            db.session.add(MedicationSchedule(
                batch_id=active.batch_id, user_id=manager.user_id,
                item_name=name, item_type="Medicine", dosage="1 g / L water",
                scheduled_date=sched,
                status="Administered" if day <= 20 else "Scheduled",
                administered_by=manager.full_name if day <= 20 else None))
        db.session.flush()

        for day_offset in range(20):
            d = date.today() - timedelta(days=19 - day_offset)
            worker = random.choice(workers)
            feed = random.choice(feeds)
            avg_weight = 40 + day_offset * random.uniform(38, 48)
            mortality = random.randint(0, 4)
            cull = random.randint(0, 1)
            feed_kg = round(avg_weight * 0.0025 * active.current_bird_count, 1)
            cause = random.choice([None, "Heat stress", "Weak chick", "Injury"])
            sub = DailyRecordSubmission(
                batch_id=active.batch_id, user_id=worker.user_id, record_date=d,
                avg_weight_g=round(avg_weight, 1), mortality=mortality, cull=cull,
                cause=cause, feed_kg=feed_kg, feed_record_id=feed.feed_record_id,
                water_consumption=f"{int(avg_weight * 0.5)} L",
                abnormal_behavior=random.choice([None, None, "Slight huddling"]),
                visible_illness=random.choice([None, None, None, "Watery eyes"]),
                remarks="Routine daily monitoring.", status="Pending",
                submitted_at=datetime.combine(d, datetime.min.time()) + timedelta(hours=17))
            db.session.add(sub)
            db.session.flush()

            if day_offset in (17, 18):
                pass
            elif day_offset == 5:
                sub.status = "Rejected"
                sub.reviewed_by = manager.user_id
                sub.reviewed_at = datetime.utcnow()
                sub.review_notes = "Weight looks off — please re-measure tomorrow."
            else:
                record_growth_data(active, worker.user_id, d,
                                   sub.avg_weight_g, sub.feed_kg, sub.feed_record_id,
                                   sub.mortality, sub.cull, sub.cause)
                sub.status = "Verified"
                sub.reviewed_by = manager.user_id
                sub.reviewed_at = datetime.utcnow()
        db.session.commit()

        for amt in [1800, 2100, 1950]:
            db.session.add(WaterExpense(
                expense_category_id=cats["Water"].expense_category_id,
                batch_id=active.batch_id,
                water_expense_amount=amt, water_expense_status="Paid"))
        for amt in [4200, 3900, 4500]:
            db.session.add(ElectricityExpense(
                expense_category_id=cats["Electricity"].expense_category_id,
                batch_id=active.batch_id,
                electricity_expense_amount=amt, electricity_expense_status="Paid"))
        for amt, prov in [(3200, "Petron Gas"), (2800, "Shellane")]:
            db.session.add(LpgExpense(
                expense_category_id=cats["LPG"].expense_category_id,
                batch_id=active.batch_id,
                lpg_expense_amount=amt, lpg_provider=prov,
                lpg_expense_status="Paid"))
        for amt in [7000, 7000]:
            db.session.add(LaborExpense(
                expense_category_id=cats["Labor"].expense_category_id,
                batch_id=active.batch_id,
                labor_expense_amount=amt, labor_expense_status="Paid"))
        for amt in [1500, 2300]:
            db.session.add(OtherExpense(
                user_id=owner.user_id,
                expense_category_id=cats["Miscellaneous"].expense_category_id,
                batch_id=active.batch_id,
                other_expense_amount=amt, other_expense_status="Pending"))
        db.session.flush()

        for b in harvested:
            kg = b.current_bird_count * random.uniform(1.4, 1.8)
            price = random.uniform(150, 175)
            db.session.add(HarvestSale(
                batch_id=b.batch_id, user_id=manager.user_id,
                sale_date=b.start_date + timedelta(days=40),
                kg_sold=round(kg, 1), price_per_kg=round(price, 2),
                total_amount=round(kg * price, 2),
                buyer=random.choice(["San Roque Market", "Balagtas Trading", "Meycauayan Buyer"]),
                remarks="Full batch sold."))
        db.session.flush()

        db.session.add(MarketPrice(
            user_id=owner.user_id,
            record_date=date.today(),
            price_per_kg=round(random.uniform(155, 175), 2),
            location="Meycauayan Public Market"))

        for b in harvested:
            db.session.add(HarvestHistory(
                batch_name=b.batch_name,
                start_date=b.start_date,
                end_date=b.start_date + timedelta(days=40),
                age=40,
                initial_count=b.initial_bird_count,
                harvest_count=b.current_bird_count,
                mortality_pct=round((b.initial_bird_count - b.current_bird_count) / b.initial_bird_count * 100, 2),
                total_deaths=b.initial_bird_count - b.current_bird_count,
                culled=0,
                adg=round(random.uniform(45, 60), 2),
                fcr=round(random.uniform(1.5, 1.8), 2),
                lw=round(random.uniform(1500, 1900), 1),
                expenses=round(random.uniform(100000, 150000), 2),
                season=b.season,
                loss_gain=round(random.uniform(-20000, 60000), 2),
                remarks="Sample harvested batch.",
            ))

        db.session.commit()

        print("Sample data seeded.")
        print("  Owner:    owner / owner123")
        print("  Manager:  manager1 / manager123")
        print("  Workers:  worker1..3 / worker123")
        print(f"  Active batch: {active.batch_name} ({active.current_bird_count} birds)")
        print(f"  Pending submissions: {DailyRecordSubmission.query.filter_by(status='Pending').count()}")


if __name__ == "__main__":
    seed()