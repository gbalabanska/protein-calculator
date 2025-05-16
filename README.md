# Protein Calculator Application

A simple SOAP web service and client application that helps users calculate their daily protein intake based on their body weight and exercise intensity.

## Features

- SOAP server built with **Spyne** serving a protein calculator service.
- Client application that asks for user input and calls the SOAP service.
- Calculates recommended protein intake with multipliers based on training intensity:
  - Low: 1.0 g per kg
  - Moderate: 1.2 g per kg
  - High: 2.0 g per kg

## Requirements

- Python 3.10 (Spyne currently incompatible with Python 3.12)
- Packages:
  - spyne
  - lxml

## Installation

Install required dependencies using pip for Python 3.10:

```bash
py -3.10 -m pip install spyne lxml


