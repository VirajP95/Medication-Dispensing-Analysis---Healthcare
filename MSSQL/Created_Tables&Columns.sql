CREATE TABLE dim_medications (
    medication_id VARCHAR(10) PRIMARY KEY,
    medication_name VARCHAR(100),
    medication_class FLOAT,
    medication_category VARCHAR(20),
    is_controlled BIT,
    requires_witness BIT
);

CREATE TABLE dim_devices (
    device_id VARCHAR(10) PRIMARY KEY,
    device_name VARCHAR(50),
    department VARCHAR(50),
    total_drawers INT,
    location_code VARCHAR(20)
);

CREATE TABLE dim_users (
    user_id VARCHAR(10) PRIMARY KEY,
    user_name VARCHAR(50),
    user_role VARCHAR(30),
    areas_assigned VARCHAR(200)
);

CREATE TABLE dim_patients (
    patient_id VARCHAR(10) PRIMARY KEY,
    patient_name VARCHAR(100),
    patient_type VARCHAR(20),
    visit_status VARCHAR(20),
    visit_date DATE,
    age FLOAT,
    gender VARCHAR(10)
);

CREATE TABLE fact_transactions (
    transaction_id VARCHAR(20) PRIMARY KEY,
    transaction_datetime DATETIME,
    transaction_type VARCHAR(20),
    transaction_duration_sec INT,
    order_number VARCHAR(10),
    quantity FLOAT,
    drawer_number VARCHAR(20),
    discrepancy_flag INT,
    witness_name VARCHAR(50),
    device_id VARCHAR(10),
    medication_id VARCHAR(10),
    user_id VARCHAR(10),
    override_user_id VARCHAR(10),
    patient_id VARCHAR(10)
);

CREATE TABLE dim_inventory (
    inventory_id VARCHAR(15) PRIMARY KEY,
    device_id VARCHAR(10),
    device_name VARCHAR(50),
    department VARCHAR(50),
    drawer_number VARCHAR(20),
    medication_id VARCHAR(10),
    medication_name VARCHAR(100),
    medication_class FLOAT,
    medication_category VARCHAR(20),
    is_controlled BIT,
    par_level FLOAT,
    current_quantity FLOAT,
    needs_restock INT
);
GO