
from datetime import date, datetime as dt, time, timedelta
from kollavarsham import Kollavarsham, KollavarshamDate
import pytz
from SiderealKundliCraft import SiderealAstroData

NAKSHATRAS_DATA = [
    {"malayalam": "Aswathi", "sanskrit": "Ashwini", "start_deg": 0.0, "end_deg": 13.333333333333334},
    {"malayalam": "Bharani", "sanskrit": "Bharani", "start_deg": 13.333333333333334, "end_deg": 26.666666666666668},
    {"malayalam": "Karthika", "sanskrit": "Krittika", "start_deg": 26.666666666666668, "end_deg": 40.0},
    {"malayalam": "Rohini", "sanskrit": "Rohini", "start_deg": 40.0, "end_deg": 53.333333333333336},
    {"malayalam": "Makayiram", "sanskrit": "Mrigashirsha", "start_deg": 53.333333333333336, "end_deg": 66.66666666666667},
    {"malayalam": "Thiruvathira", "sanskrit": "Ardra", "start_deg": 66.66666666666667, "end_deg": 80.0},
    {"malayalam": "Punartham", "sanskrit": "Punarvasu", "start_deg": 80.0, "end_deg": 93.33333333333334},
    {"malayalam": "Pooyam", "sanskrit": "Pushya", "start_deg": 93.33333333333334, "end_deg": 106.66666666666667},
    {"malayalam": "Ayilyam", "sanskrit": "Ashlesha", "start_deg": 106.66666666666667, "end_deg": 120.0},
    {"malayalam": "Makam", "sanskrit": "Magha", "start_deg": 120.0, "end_deg": 133.33333333333334},
    {"malayalam": "Pooram", "sanskrit": "Purva Phalguni", "start_deg": 133.33333333333334, "end_deg": 146.66666666666669},
    {"malayalam": "Uthram", "sanskrit": "Uttara Phalguni", "start_deg": 146.66666666666669, "end_deg": 160.0},
    {"malayalam": "Atham", "sanskrit": "Hasta", "start_deg": 160.0, "end_deg": 173.33333333333334},
    {"malayalam": "Chithira", "sanskrit": "Chitra", "start_deg": 173.33333333333334, "end_deg": 186.66666666666669},
    {"malayalam": "Chothi", "sanskrit": "Swati", "start_deg": 186.66666666666669, "end_deg": 200.0},
    {"malayalam": "Vishakam", "sanskrit": "Vishakha", "start_deg": 200.0, "end_deg": 213.33333333333334},
    {"malayalam": "Anizham", "sanskrit": "Anuradha", "start_deg": 213.33333333333334, "end_deg": 226.66666666666669},
    {"malayalam": "Thriketta", "sanskrit": "Jyeshtha", "start_deg": 226.66666666666669, "end_deg": 240.0},
    {"malayalam": "Moolam", "sanskrit": "Mula", "start_deg": 240.0, "end_deg": 253.33333333333334},
    {"malayalam": "Pooradam", "sanskrit": "Purva Ashadha", "start_deg": 253.33333333333334, "end_deg": 266.6666666666667},
    {"malayalam": "Uthradam", "sanskrit": "Uttara Ashadha", "start_deg": 266.6666666666667, "end_deg": 280.0},
    {"malayalam": "Thiruvonam", "sanskrit": "Shravana", "start_deg": 280.0, "end_deg": 293.3333333333333},
    {"malayalam": "Avittam", "sanskrit": "Dhanishtha", "start_deg": 293.3333333333333, "end_deg": 306.66666666666663},
    {"malayalam": "Chathayam", "sanskrit": "Shatabhisha", "start_deg": 306.66666666666663, "end_deg": 320.0},
    {"malayalam": "Pooruruttathi", "sanskrit": "Purva Bhadrapada", "start_deg": 320.0, "end_deg": 333.3333333333333},
    {"malayalam": "Uthrattathi", "sanskrit": "Uttara Bhadrapada", "start_deg": 333.3333333333333, "end_deg": 346.66666666666663},
    {"malayalam": "Revathi", "sanskrit": "Revati", "start_deg": 346.66666666666663, "end_deg": 360.0}
]

#  Default Astronomical Calculation Parameters
DEFAULT_LATITUDE = 10.5276
DEFAULT_LONGITUDE = 76.2144
DEFAULT_UTC_OFFSET_HOURS = 5
DEFAULT_UTC_OFFSET_MINUTES = 30
DEFAULT_AYANAMSA_TYPE = "ay_lahiri"

def get_sun_sidereal_longitude_accurate(datetime_obj: dt, latitude: float, longitude: float,
                                        utc_offset_hours: int, utc_offset_minutes: int,
                                        ayanamsa_type: str = "ay_lahiri") -> float | None:

    try:
        astro_data = SiderealAstroData.AstroData(
            datetime_obj.year, datetime_obj.month, datetime_obj.day,
            datetime_obj.hour, datetime_obj.minute, datetime_obj.second,
            utc_offset_hours, utc_offset_minutes,
            latitude, longitude,
            ayanamsa=ayanamsa_type
        )
        planets_data = astro_data.planets_rashi()
        sun_longitude = planets_data['sun']['lon']
        return sun_longitude
    except Exception as e:
        print(f"Error calculating Sun's sidereal longitude for {datetime_obj} using SiderealKundliCraft: {e}")
        return None

def get_current_nakshatra_details(gregorian_date_input: date) -> dict | None:

    calc_datetime = dt(gregorian_date_input.year, gregorian_date_input.month, gregorian_date_input.day, 6, 0, 0)
    sun_lon_sidereal = get_sun_sidereal_longitude_accurate(
        calc_datetime,
        DEFAULT_LATITUDE, DEFAULT_LONGITUDE,
        DEFAULT_UTC_OFFSET_HOURS, DEFAULT_UTC_OFFSET_MINUTES,
        DEFAULT_AYANAMSA_TYPE
    )
    if sun_lon_sidereal is None:
        return None
    sun_lon_sidereal %= 360.0
    for nakshatra_info in NAKSHATRAS_DATA:
        start_deg = nakshatra_info["start_deg"]
        end_deg = nakshatra_info["end_deg"]
        if start_deg <= sun_lon_sidereal < end_deg:
            return nakshatra_info
    print(f"Warning: Sidereal longitude {sun_lon_sidereal} did not fall into any defined Nakshatra span.")
    return None

def gregorian_to_malayalam_date(gregorian_date_input: date) -> dict:

    kollavarsham_converter = Kollavarsham(
        latitude=DEFAULT_LATITUDE,
        longitude=DEFAULT_LONGITUDE,
        system='SuryaSiddhanta'
    )
    datetime_input_obj: dt
    if isinstance(gregorian_date_input, date) and not isinstance(gregorian_date_input, dt):
        tz = pytz.timezone('Asia/Kolkata')
        datetime_input_obj = tz.localize(dt.combine(gregorian_date_input, time.min))
    elif isinstance(gregorian_date_input, dt):
        if gregorian_date_input.tzinfo is None or gregorian_date_input.tzinfo.utcoffset(gregorian_date_input) is None:
            tz = pytz.timezone('Asia/Kolkata')
            datetime_input_obj = tz.localize(gregorian_date_input)
        else:
            tz = pytz.timezone('Asia/Kolkata')
            datetime_input_obj = gregorian_date_input.astimezone(tz)
    else:
        raise TypeError("Input must be a datetime.date or datetime.datetime object.")
    kv_date: KollavarshamDate = kollavarsham_converter.from_gregorian_date(date=datetime_input_obj)
    return {
        "malayalam_month": kv_date.ml_masa_name,
        "malayalam_day": kv_date.date,
        "kollavarsham_year": kv_date.year
    }

def generate_njattuvela_calendar(target_gregorian_year: int) -> list:
    njattuvela_periods = []
    start_of_year = date(target_gregorian_year, 1, 1)
    end_of_year = date(target_gregorian_year, 12, 31)
    current_gregorian_date = start_of_year
    previous_nakshatra_details = get_current_nakshatra_details(current_gregorian_date)
    if previous_nakshatra_details is None:
        raise ValueError(f"Could not determine initial Nakshatra for {current_gregorian_date} using accurate method.")
    current_period_start_date = start_of_year
    while current_gregorian_date <= end_of_year:
        today_nakshatra_details = get_current_nakshatra_details(current_gregorian_date)
        if today_nakshatra_details is None:
            print(f"Warning: Accurate Nakshatra determination failed for {current_gregorian_date}. Using previous day's details.")
            today_nakshatra_details = previous_nakshatra_details
        if today_nakshatra_details['malayalam'] != previous_nakshatra_details['malayalam']:
            period_end_date = current_gregorian_date - timedelta(days=1)
            duration = (period_end_date - current_period_start_date).days + 1
            malayalam_start_info = gregorian_to_malayalam_date(current_period_start_date)
            malayalam_end_info = gregorian_to_malayalam_date(period_end_date)
            njattuvela_periods.append({
                "malayalam_name": previous_nakshatra_details['malayalam'],
                "sanskrit_name": previous_nakshatra_details['sanskrit'],
                "start_date_gregorian": current_period_start_date,
                "end_date_gregorian": period_end_date,
                "duration_days": duration,
                "malayalam_start_info": malayalam_start_info,
                "malayalam_end_info": malayalam_end_info,
            })
            current_period_start_date = current_gregorian_date
            previous_nakshatra_details = today_nakshatra_details
        current_gregorian_date += timedelta(days=1)
    duration_last_period = (end_of_year - current_period_start_date).days + 1
    malayalam_start_info_last = gregorian_to_malayalam_date(current_period_start_date)
    malayalam_end_info_last = gregorian_to_malayalam_date(end_of_year)
    njattuvela_periods.append({
        "malayalam_name": previous_nakshatra_details['malayalam'],
        "sanskrit_name": previous_nakshatra_details['sanskrit'],
        "start_date_gregorian": current_period_start_date,
        "end_date_gregorian": end_of_year,
        "duration_days": duration_last_period,
        "malayalam_start_info": malayalam_start_info_last,
        "malayalam_end_info": malayalam_end_info_last,
    })
    return njattuvela_periods

def format_malayalam_period_string(start_info: dict, end_info: dict) -> str:

    if start_info['malayalam_month'] == end_info['malayalam_month'] and \
       start_info['kollavarsham_year'] == end_info['kollavarsham_year']:
        return f"{start_info['malayalam_month']} {start_info['malayalam_day']}-{end_info['malayalam_day']} ({start_info['kollavarsham_year']})"
    else:
        return (f"{start_info['malayalam_month']} {start_info['malayalam_day']} ({start_info['kollavarsham_year']}) - "
                f"{end_info['malayalam_month']} {end_info['malayalam_day']} ({end_info['kollavarsham_year']})")

def print_njattuvela_table(calendar_data: list, target_year: int):

    print(f"\n--- Njattuvela Calendar for Gregorian Year: {target_year} (using SiderealKundliCraft) ---")
    header = {
        "mal_name": "Malayalam Name", "san_name": "Sanskrit Name",
        "greg_start": "Start Date", "greg_end": "End Date",
        "duration": "Duration", "mal_period": "Malayalam Period"
    }
    w = {
        "mal_name": 15, "san_name": 15, "greg_start": 12,
        "greg_end": 12, "duration": 8, "mal_period": 45
    }
    print(f"{header['mal_name']:<{w['mal_name']}} | "
          f"{header['san_name']:<{w['san_name']}} | "
          f"{header['greg_start']:<{w['greg_start']}} | "
          f"{header['greg_end']:<{w['greg_end']}} | "
          f"{header['duration']:<{w['duration']}} | "
          f"{header['mal_period']:<{w['mal_period']}}")
    total_width = sum(w.values()) + (len(w) - 1) * 3
    print("-" * total_width)
    if not calendar_data:
        print(f"No Njattuvela calendar data generated for {target_year}.")
        return
    for period in calendar_data:
        greg_start_str = period['start_date_gregorian'].isoformat()
        greg_end_str = period['end_date_gregorian'].isoformat()
        duration_str = f"{period['duration_days']} days"
        malayalam_period_str = format_malayalam_period_string(
            period['malayalam_start_info'], period['malayalam_end_info']
        )
        print(f"{period['malayalam_name']:<{w['mal_name']}} | "
              f"{period['sanskrit_name']:<{w['san_name']}} | "
              f"{greg_start_str:<{w['greg_start']}} | "
              f"{greg_end_str:<{w['greg_end']}} | "
              f"{duration_str:<{w['duration']}} | "
              f"{malayalam_period_str:<{w['mal_period']}}")

# The main execution block has been removed to allow this file to be used as a module.
# The web interface for this script is now in `app.py`.
