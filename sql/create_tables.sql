-- =========================================================
-- AIRLINE DATA ANALYTICS
-- DATABASE SCHEMA DEFINITION (PostgreSQL)
-- =========================================================

DROP TABLE IF EXISTS airport_lookup CASCADE;

CREATE TABLE airport_lookup (
    airport_code VARCHAR(10) PRIMARY KEY,
    airport_name VARCHAR(150) NOT NULL,
    airport_city VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    latitude NUMERIC(10, 6) NOT NULL,
    longitude NUMERIC(10, 6) NOT NULL
);

DROP TABLE IF EXISTS airline_data CASCADE;

CREATE TABLE airline_data (
    flight_number VARCHAR(50) NOT NULL,
    flight_date DATE NOT NULL,
    origin VARCHAR(10) NOT NULL REFERENCES airport_lookup(airport_code),
    destination VARCHAR(10) NOT NULL REFERENCES airport_lookup(airport_code),
    route VARCHAR(50) NOT NULL,
    aircraft_type VARCHAR(100) NOT NULL,
    aircraft_capacity INTEGER NOT NULL,
    passengers INTEGER NOT NULL,
    load_factor NUMERIC(10, 4) NOT NULL,
    flight_hours NUMERIC(10, 2) NOT NULL,
    season VARCHAR(50) NOT NULL,
    route_category VARCHAR(50) NOT NULL,
    demand_level VARCHAR(50) NOT NULL,
    ticket_revenue NUMERIC(15, 2) NOT NULL,
    ancillary_revenue NUMERIC(15, 2) NOT NULL,
    total_revenue NUMERIC(15, 2) NOT NULL,
    fuel_cost NUMERIC(15, 2) NOT NULL,
    maintenance_cost NUMERIC(15, 2) NOT NULL,
    crew_cost NUMERIC(15, 2) NOT NULL,
    depreciation_cost NUMERIC(15, 2) NOT NULL,
    insurance_cost NUMERIC(15, 2) NOT NULL,
    airport_fees NUMERIC(15, 2) NOT NULL,
    catering_cost NUMERIC(15, 2) NOT NULL,
    handling_cost NUMERIC(15, 2) NOT NULL,
    navigation_fees NUMERIC(15, 2) NOT NULL,
    sales_distribution_cost NUMERIC(15, 2) NOT NULL,
    passenger_service_cost NUMERIC(15, 2) NOT NULL,
    overhead_cost NUMERIC(15, 2) NOT NULL,
    marketing_cost NUMERIC(15, 2) NOT NULL,
    it_systems_cost NUMERIC(15, 2) NOT NULL,
    total_cost NUMERIC(15, 2) NOT NULL,
    profit NUMERIC(15, 2) NOT NULL,
    profit_margin NUMERIC(10, 4) NOT NULL,
    year INTEGER NOT NULL,
    quarter INTEGER NOT NULL,
    month_number INTEGER NOT NULL,
    month VARCHAR(20) NOT NULL,
    day INTEGER NOT NULL,
    day_name VARCHAR(20) NOT NULL
);

CREATE INDEX idx_airline_date ON airline_data(flight_date);
CREATE INDEX idx_airline_route ON airline_data(route);
CREATE INDEX idx_airline_aircraft ON airline_data(aircraft_type);
