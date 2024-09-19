# ouster_medata_retrieval
Ouster Sensor Metadata Retrieval Tool  A simple Python script to retrieve metadata from an Ouster LiDAR sensor using its HTTP API. The script fetches the sensor's metadata and saves it to a timestamped JSON file, aiding in troubleshooting and configuration management.
## Features

- **Retrieve Sensor Metadata**: Fetches detailed metadata from an Ouster sensor using its HTTP API.
- **Save to JSON File**: Saves the retrieved metadata to a JSON file named with the current date and time.
- **Troubleshooting Aid**: Useful for diagnosing issues, verifying configurations, and sharing sensor information with support teams.
- **Easy to Use**: Simple command-line interface that requires minimal setup.

## Requirements

- **Python Version**: Python 3.6 or higher
- **Python Libraries**:
  - `requests`

## Installation

### **1. Clone the Repository**

```bash
git clone https://github.com/thomasrcezar/ouster_medata_retrieval.git