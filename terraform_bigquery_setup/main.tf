provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_bigquery_dataset" "tapfiliate_dataset" {
  dataset_id = "tapfiliate_data"
  friendly_name = "Tapfiliate Conversions Data"
  description   = "Stores conversions data fetched from the Tapfiliate API"
  location      = var.region
}

resource "google_bigquery_table" "conversions_table" {
  dataset_id = google_bigquery_dataset.tapfiliate_dataset.dataset_id
  table_id   = "conversions"

  schema = file("schema.json")
  
  time_partitioning {
    type  = "DAY"
    field = "created_date"
  }
}
