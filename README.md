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

To run this script, you need Python 3 and the following libraries:

*   `kollavarsham`
*   `SiderealKundliCraft`
*   `pytz`

You can install these dependencies using pip:


pip install kollavarsham SiderealKundliCraft pytz
Usage
Save the script as njattuvela_calendar.py (or your preferred filename).

Open a terminal or command prompt.

Run the script using Python:

python njattuvela_calendar.py
By default, the script generates the calendar for the year 2024. You can change the TARGET_YEAR variable within the script's if __name__ == "__main__": block to generate the calendar for a different year.

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
