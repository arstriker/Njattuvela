# Njattuvela Calendar Generator

## Description

This Python script generates a Njattuvela calendar for a specified Gregorian year. The Njattuvela calendar is a traditional Kerala system that tracks the Sun's transit through the 27 Nakshatras (star constellations). It is historically significant for agricultural planning and astrological purposes.

This script calculates the start and end dates of each Njattuvela period, its duration, and the corresponding Malayalam calendar dates.

## Features

*   Calculates Njattuvela periods based on the Sun's transit through the 27 Nakshatras.
*   Provides accurate Gregorian start and end dates for each Njattuvela.
*   Converts Gregorian dates to the traditional Malayalam calendar (Kollavarsham), including month name (in Malayalam script), day, and year.
*   Displays the calendar in a clear, formatted table.
*   Utilizes specialized libraries for higher accuracy:
    *   `SiderealKundliCraft` for precise astronomical calculations (solar longitude, using Lahiri Ayanamsa by default).
    *   `kollavarsham` for accurate Malayalam calendar conversions (using Surya Siddhanta system by default for Kerala coordinates).
*   Includes both Malayalam and Sanskrit names for each Nakshatra.

## Requirements

To run this project, you need Python 3 and the libraries listed in `requirments.txt`.

You can install these dependencies using pip:
```bash
pip install -r requirments.txt
```

## Web Interface Usage

This project includes a user-friendly web interface. To run it, follow these steps:

1.  **Install Dependencies:**
    Make sure you have installed all the required packages:
    ```bash
    pip install -r requirments.txt
    ```

2.  **Run the Web Server:**
    Start the Flask development server with the following command:
    ```bash
    python3.12 app.py
    ```
    *Note: It is recommended to use `python3.12`. If that is not available, you can try `python3`.*

3.  **Access the Application:**
    Open your web browser and navigate to:
    [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

    You can then enter a year in the input field and click "Generate Calendar" to see the results.

## Command-Line Usage (Legacy)

The original command-line script `njattuvela_calendar.py` is still available but is no longer the primary way to run the program. To use it, you would need to restore the main execution block in the script.

Output Format
The script will print a table to the console with the following columns:

Njattuvela Name (Malayalam): The Malayalam name of the Nakshatra (e.g., അശ്വതി).

Sanskrit Name: The traditional Sanskrit name for the Nakshatra (e.g., Ashwini).

Start Date (Greg.): The Gregorian calendar date (YYYY-MM-DD) when the Sun enters this Nakshatra.

End Date (Greg.): The Gregorian calendar date (YYYY-MM-DD) when the Sun leaves this Nakshatra.

Duration (Days): The duration of the Njattuvela period in days.

Malayalam Period: The start and end of the Njattuvela period in the Malayalam calendar, formatted as:

മലയാളം മാസം ദിവസം-ദിവസം (കൊല്ലവർഷം) (e.g., ചിങ്ങം 1-14 (1199)) if within the same month and year.

മാസം1 ദിവസം1 (വർഷം1) - മാസം2 ദിവസം2 (വർഷം2) (e.g., ചിങ്ങം 28 (1199) - കന്നി 10 (1199)) if spanning months or years.

Astronomical Basis and Accuracy

Solar Longitude and Nakshatra Transits: Calculated using the SiderealKundliCraft library, which provides sidereal astronomical data. By default, it uses the Lahiri Ayanamsa.
Malayalam Calendar Conversion: Performed using the kollavarsham library, which implements the traditional Surya Siddhanta system for calendar calculations, configured for Kerala's geographical coordinates.
Calculation Time: The script determines the Nakshatra for each day based on the Sun's position at a fixed time (06:00 AM IST). This is a common practice but means that the exact moment of transit might vary slightly.
While these libraries provide a high degree of accuracy, traditional Panchangams can sometimes have minor variations due to different schools of thought or specific local adjustments.

Limitations
The accuracy is dependent on the underlying astronomical models and data used by the SiderealKundliCraft and kollavarsham libraries.
For critical religious or astrological applications, it is always recommended to consult with a traditional Panchangam expert or a localized, authoritative Panchangam.
