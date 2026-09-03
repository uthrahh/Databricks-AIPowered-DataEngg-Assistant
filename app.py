import streamlit as st
import time
from datetime import datetime

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Databricks AI Data Engineering Assistant",
    page_icon="⚙️",
    layout="wide"
)

# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "analysis" not in st.session_state:
    st.session_state.analysis = None

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------
st.markdown("""
<style>
    .main {
        padding-top: 1rem;
    }

    .agent-card {
        border: 1px solid #444;
        border-radius: 10px;
        padding: 15px;
        margin: 8px 0;
    }

    .status {
        font-size: 14px;
        font-weight: 600;
    }

    .success {
        color: #00C853;
    }

    .warning {
        color: #FFAB00;
    }

    .danger {
        color: #FF5252;
    }

    .info {
        color: #42A5F5;
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.title("Databricks AI Data Engineering Assistant")
st.caption(
    "AI-powered pipeline monitoring, diagnosis, prediction and self-healing"
)

st.divider()


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
with st.sidebar:

    st.header("System Status")

    st.success("Databricks Connected")
    st.success("Unity Catalog Connected")
    st.success("Model Serving Online")
    st.success("LangGraph Supervisor Online")

    st.divider()

    st.subheader("Agents")

    agents = [
        "Supervisor Agent",
        "SLA Agent",
        "Data Quality Agent",
        "Pipeline Agent",
        "Config Agent",
        "RCA Agent",
        "Prediction Agent",
        "Simulation Agent",
        "Recovery Agent",
        "Validation Agent",
        "Notification Agent"
    ]

    for agent in agents:
        st.write("●", agent)

    st.divider()

    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.session_state.analysis = None
        st.rerun()


# ---------------------------------------------------------
# AGENT PIPELINE
# ---------------------------------------------------------
st.subheader("Agent Workflow")

workflow = [
    "Chat",
    "Understand",
    "Diagnose",
    "Predict",
    "Simulate",
    "Approval",
    "Execute",
    "Validate",
    "Learn"
]

cols = st.columns(len(workflow))

for i, step in enumerate(workflow):
    with cols[i]:
        st.metric(
            label=step,
            value="●",
        )


# ---------------------------------------------------------
# CHAT HISTORY
# ---------------------------------------------------------
st.divider()
st.subheader("AI Assistant")

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ---------------------------------------------------------
# AGENT EXECUTION
# ---------------------------------------------------------
def run_agent_workflow(user_query):

    results = {}

    # -----------------------------
    # SUPERVISOR
    # -----------------------------
    with st.status("Supervisor Agent: Understanding request...", expanded=True):

        time.sleep(0.5)

        results["intent"] = (
            "Pipeline monitoring / SLA analysis"
        )

        st.write("Intent detected:", results["intent"])


    # -----------------------------
    # SLA AGENT
    # -----------------------------
    with st.status("SLA Agent: Predicting pipeline completion...", expanded=True):

        time.sleep(0.7)

        results["sla_probability"] = 87

        st.warning(
            "87% probability of SLA breach detected."
        )

        st.write("Current processing rate: **18K records/min**")
        st.write("Expected volume: **12.4M records**")
        st.write("Historical average: **8.2M records**")
        st.write("Estimated completion: **07:42 AM**")
        st.write("SLA: **07:00 AM**")


    # -----------------------------
    # DATA QUALITY AGENT
    # -----------------------------
    with st.status("Data Quality Agent: Checking data health...", expanded=True):

        time.sleep(0.6)

        results["data_health"] = 82

        st.metric(
            "Data Health Score",
            "82 / 100"
        )

        st.write("Missing records: **1.8%**")
        st.write("Duplicate records: **0.3%**")
        st.write("Schema violations: **2**")


    # -----------------------------
    # PIPELINE AGENT
    # -----------------------------
    with st.status("Pipeline Agent: Inspecting pipeline...", expanded=True):

        time.sleep(0.6)

        results["pipeline_status"] = "Degraded"

        st.warning(
            "Pipeline processing 2.4× slower than normal."
        )

        st.write("Current throughput: **18K records/min**")
        st.write("Normal throughput: **43K records/min**")


    # -----------------------------
    # GENIE
    # -----------------------------
    with st.status("Databricks Genie: Querying governed data...", expanded=True):

        time.sleep(0.6)

        results["volume_anomaly"] = True

        st.info(
            "Today's data volume is 3.1× higher than the historical average."
        )


    # -----------------------------
    # RCA
    # -----------------------------
    with st.status("RCA Agent: Determining root cause...", expanded=True):

        time.sleep(0.8)

        results["root_cause"] = (
            "Unexpected increase in POS transaction volume "
            "combined with insufficient compute capacity."
        )

        st.error(
            "Root Cause Identified"
        )

        st.write(results["root_cause"])


    # -----------------------------
    # PREDICTION
    # -----------------------------
    with st.status("Prediction Agent: Forecasting failure...", expanded=True):

        time.sleep(0.6)

        results["prediction"] = (
            "Pipeline is likely to breach SLA unless compute "
            "capacity is increased."
        )

        st.warning(results["prediction"])


    # -----------------------------
    # RECOVERY
    # -----------------------------
    with st.status("Recovery Agent: Generating remediation...", expanded=True):

        time.sleep(0.6)

        results["recommendation"] = (
            "Increase compute capacity by 2× and restart the "
            "affected pipeline task."
        )

        st.success(
            "Recommended Action"
        )

        st.write(results["recommendation"])


    return results


# ---------------------------------------------------------
# CHAT INPUT
# ---------------------------------------------------------
user_query = st.chat_input(
    "Ask about your pipelines, data quality, SLA, failures..."
)

if user_query:

    # User message
    st.session_state.messages.append({
        "role": "user",
        "content": user_query
    })

    with st.chat_message("user"):
        st.markdown(user_query)

    # AI response
    with st.chat_message("assistant"):

        results = run_agent_workflow(user_query)

        st.session_state.analysis = results

        st.markdown(
            "### Analysis Complete"
        )

        st.markdown(
            f"""
**Root Cause:**  
{results['root_cause']}

**Recommended Action:**  
{results['recommendation']}
"""
        )

        st.session_state.messages.append({
            "role": "assistant",
            "content": (
                f"Root Cause: {results['root_cause']}\n\n"
                f"Recommended Action: {results['recommendation']}"
            )
        })


# ---------------------------------------------------------
# APPROVAL SECTION
# ---------------------------------------------------------
if st.session_state.analysis:

    st.divider()

    st.subheader("Recommended Remediation")

    results = st.session_state.analysis

    col1, col2 = st.columns([3, 1])

    with col1:

        st.warning(
            f"""
**Proposed action:**  
{results['recommendation']}

**Expected impact:**  
Restore pipeline throughput and reduce probability of SLA breach.
"""
        )

    with col2:

        approve = st.button(
            "Approve & Execute",
            type="primary",
            use_container_width=True
        )

        reject = st.button(
            "Reject",
            use_container_width=True
        )

    # -----------------------------------------------------
    # EXECUTION
    # -----------------------------------------------------
    if approve:

        with st.status(
            "Executing remediation...",
            expanded=True
        ):

            st.write("Submitting Databricks Job...")
            time.sleep(1)

            st.write("Scaling compute...")
            time.sleep(1)

            st.write("Restarting pipeline task...")
            time.sleep(1)

            st.write("Running validation checks...")
            time.sleep(1)

            st.success(
                "Remediation executed successfully."
            )

        # -------------------------------------------------
        # VALIDATION
        # -------------------------------------------------
        st.subheader("Validation")

        validation_cols = st.columns(4)

        validation_cols[0].metric(
            "DQ Checks",
            "27/27"
        )

        validation_cols[1].metric(
            "Pipeline Status",
            "Healthy"
        )

        validation_cols[2].metric(
            "Throughput",
            "46K/min"
        )

        validation_cols[3].metric(
            "SLA Risk",
            "12%"
        )

        st.success(
            "RESOLVED — Pipeline is operating within SLA."
        )