import os
import requests
import pandas as pd
import streamlit as st

# Configure Streamlit page layout
st.set_page_config(
    page_title="SuperKart Sales Prediction Dashboard",
    page_icon="🛒",
    layout="wide"
)

# Define backend API URL from environment variable or default local container port
BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:7860")

st.title("🛒 SuperKart Sales Revenue Prediction Engine")
st.markdown("Forecast sales revenue for SuperKart store locations using single or batch inference.")

# Create tabs for Single and Batch Predictions
tab1, tab2 = st.tabs(["🎯 Single Product Prediction", "📁 Batch Prediction (CSV)"])

with tab1:
    st.header("Single Product Sales Inference")
    st.write("Enter product and store parameters to predict expected quarterly revenue.")

    col1, col2, col3 = st.columns(3)

    with col1:
        product_weight = st.number_input("Product Weight", min_value=1.0, max_value=30.0, value=12.5, step=0.1)
        product_sugar_content = st.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"])
        product_allocated_area = st.number_input("Product Display Area Ratio", min_value=0.0, max_value=0.5, value=0.05, step=0.005)
        product_mrp = st.number_input("Product MRP ($)", min_value=10.0, max_value=500.0, value=140.0, step=1.0)

    with col2:
        store_size = st.selectbox("Store Size", ["Small", "Medium", "High"])
        store_location_city_type = st.selectbox("Store City Tier", ["Tier 1", "Tier 2", "Tier 3"])
        store_type = st.selectbox("Store Type", ["Food Mart", "Supermarket Type1", "Supermarket Type2", "Departmental Store"])

    with col3:
        product_id_char = st.selectbox("Product Category Prefix", ["FD", "DR", "NC"])
        store_age_years = st.slider("Store Operational Age (Years)", min_value=1, max_value=40, value=15)
        product_type_category = st.selectbox("Product Type Category (Perishable / Non-Perishable)",
            ["Perishables", "Non Perishables"])

    if st.button("Predict Sales Revenue", type="primary"):
        # Construct input payload matching the encoded training features
        payload = {
            "Product_Weight": product_weight,
            "Product_Sugar_Content": product_sugar_content,
            "Product_Allocated_Area": product_allocated_area,
            "Product_MRP": product_mrp,
            "Store_Size": store_size,
            "Store_Location_City_Type": store_location_city_type,
            "Store_Type": store_type,
            "Product_Id_char": product_id_char,
            "Store_Age_Years": store_age_years,
            "Product_Type_Category": product_type_category
        }

        try:
            response = requests.post(f"{BACKEND_URL}/v1/predict", json=payload)
            if response.status_code == 200:
                result = response.json()
                predicted_sales = result.get("prediction", 0.0)
                st.success(f"### Predicted Quarterly Sales Total: **${predicted_sales:,.2f}**")
            else:
                st.error(f"API Error ({response.status_code}): {response.text}")
        except Exception as e:
            st.error(f"Failed to connect to backend API: {str(e)}")

with tab2:
    st.header("Batch Sales Inference")
    st.write("Upload a CSV file containing multiple product records for batch evaluation.")

    uploaded_file = st.file_uploader("Upload Batch CSV Data", type=["csv"])

    if uploaded_file is not None:
        st.subheader("Preview Uploaded Input Data")
        input_df = pd.read_csv(uploaded_file)
        st.dataframe(input_df.head(10))

        if st.button("Run Batch Inference", type="primary"):
            uploaded_file.seek(0)
            files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "text/csv")}

            try:
                response = requests.post(f"{BACKEND_URL}/v1/predictbatch", files=files)
                if response.status_code == 200:
                    predictions_dict = response.json()
                    input_df["Predicted_Product_Store_Sales_Total"] = input_df.index.astype(str).map(predictions_dict)
                    st.subheader("Batch Prediction Results")
                    st.dataframe(input_df)

                    # Download results
                    csv_data = input_df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="Download Predictions CSV",
                        data=csv_data,
                        file_name="superkart_batch_predictions.csv",
                        mime="text/csv"
                    )
                else:
                    st.error(f"API Error ({response.status_code}): {response.text}")
            except Exception as e:
                st.error(f"Failed to connect to backend API: {str(e)}")
