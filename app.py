import logging
from flask import Flask, render_template, request
from njattuvela_calendar import generate_njattuvela_calendar, format_malayalam_period_string

logging.basicConfig(filename='app.log', level=logging.DEBUG)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    logging.info("Index function called")
    calendar_data = None
    year = None
    if request.method == 'POST':
        try:
            year = int(request.form['year'])
            logging.info(f"Year received: {year}")
            raw_calendar_data = generate_njattuvela_calendar(year)
            logging.info("Calendar data generated")
            # Format the data for JSON serialization
            calendar_data = []
            for period in raw_calendar_data:
                period['malayalam_period_str'] = format_malayalam_period_string(
                    period['malayalam_start_info'], period['malayalam_end_info']
                )
                # Convert date objects to strings
                period['start_date_gregorian'] = period['start_date_gregorian'].isoformat()
                period['end_date_gregorian'] = period['end_date_gregorian'].isoformat()
                calendar_data.append(period)
            logging.info("Calendar data formatted for JSON")
            import json
            calendar_data_json = json.dumps(calendar_data)
            logging.debug(f"Calendar data JSON: {calendar_data_json}")
        except Exception as e:
            logging.error(f"Error processing request: {e}")
            calendar_data_json = None

    return render_template('index.html', calendar_data_json=calendar_data_json, year=year)

if __name__ == '__main__':
    logging.info("Starting Flask server")
    app.run(debug=True)
