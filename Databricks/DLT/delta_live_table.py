import dlt


# -- dimuser ----

@dlt.table
def dimuser_stg():
    df=spark.readStream.table("spotifi.silver.dimuser")
    return df

dlt.create_streaming_table("dimuser")

dlt.create_auto_cdc_flow(
    target="dimuser",
    source="dimuser_stg",
    keys=["user_id"],
    sequence_by="updated_at",
    stored_as_scd_type=2,
    track_history_except_column_list=None,
    name=None,
    ONCE=False
)
# ---- dimtrack ----

@dlt.table
def dimtrack_stg():
    df=spark.readStream.table("spotifi.silver.dimtrack")
    return df

dlt.create_streaming_table("dimtrack")

dlt.create_auto_cdc_flow(
    target="dimtrack",
    source="dimtrack_stg",
    keys=["track_id"],
    sequence_by="updated_at",
    stored_as_scd_type=2,
    track_history_except_column_list=None,
    name=None,
    ONCE=False
)

# --- dimdate ---

@dlt.table
def dimdate_stg():
    df=spark.readStream.table("spotifi.silver.dimdate")
    return df

dlt.create_streaming_table("dimdate")

dlt.create_auto_cdc_flow(
    target="dimdate",
    source="dimdate_stg",
    keys=["date_key"],
    sequence_by="date",
    stored_as_scd_type=2,
    track_history_except_column_list=None,
    name=None,
    ONCE=False
)


# --- factStream ----

# 

@dlt.table
def factstream_stg():
    df=spark.readStream.table("spotifi.silver.factstream")
    return df

dlt.create_streaming_table("factstream")

dlt.create_auto_cdc_flow(  
    target="factstream",
    source="factstream_stg",
    keys=["stream_id"],
    sequence_by="stream_timestamp",
    stored_as_scd_type=1,
    track_history_except_column_list=None,
    name=None,
    ONCE=False
)
