# Network Intelligence App

## Overview

This application gathers network connection information (active and past connectivity from logs), runs the list of unique public network information over a threat intelligence platform, and identifies potential exposures or risks.

## Setup

1. **Clone the repository**:

   ```sh
   git clone https://github.com/GeorgiVld/network-intelligence-app
   cd network-intelligence-app/src
   ```

2. **Create a virtual environment and activate it**:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the requirements**:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Run the script**:

   ```sh
   python network_intelligence.py
   ```

## Screenshots

![Placeholder](screenshots/placeholder.png)

## Features

- Gather active and past network connectivity information.
- Run threat intelligence checks using the free platform AbuseIPDB.
- OS agnostic: Can run on Windows, MacOS, and Linux.
