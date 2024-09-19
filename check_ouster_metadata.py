#!/usr/bin/env python3

import argparse
import requests
import sys
import json
from datetime import datetime

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Check Ouster sensor metadata.')
    parser.add_argument('sensor_ip', help='IP address of the Ouster sensor')
    args = parser.parse_args()

    sensor_ip = args.sensor_ip

    # Construct the API endpoint URL
    url = f'http://{sensor_ip}/api/v1/sensor/metadata'

    try:
        # Make the HTTP GET request to the sensor's API
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.exceptions.RequestException as e:
        print(f'Error connecting to sensor at {sensor_ip}: {e}', file=sys.stderr)
        sys.exit(1)

    try:
        # Parse the JSON response
        metadata = response.json()
    except ValueError as e:
        print(f'Error parsing JSON response: {e}', file=sys.stderr)
        sys.exit(1)

    # Display the metadata
    print('Sensor Metadata:')
    for key, value in metadata.items():
        print(f'{key}: {value}')

    # Get current date and time
    now = datetime.now()
    # Format date and time into a safe filename
    # Sanitize the sensor IP for filename (replace dots with underscores)
    safe_sensor_ip = sensor_ip.replace('.', '_')
    # Include sensor IP in the filename
    filename = f"{now.strftime('%d-%m-%Y_%H-%M-%S')}_{safe_sensor_ip}.json"

    try:
        # Write metadata to JSON file
        with open(filename, 'w') as f:
            json.dump(metadata, f, indent=4)
        print(f'Metadata saved to {filename}')
    except IOError as e:
        print(f'Error writing to file {filename}: {e}', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
