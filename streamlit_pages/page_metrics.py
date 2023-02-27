
import streamlit as st


def page_eval():
    st.title("Metrics of the model")
    if st.session_state.get('evaluator_instance', None) is None:
        st.warning("You must first fit a model !")
    else:
        evaluator = st.session_state["evaluator_instance"]
        metrics = evaluator.get_metrics()
        for metric_name, metric in zip(["mae", "mse", "rmse", "mape", "r2"], metrics):
            st.write(f"{metric_name} = {metric}")

        st.plotly_chart(evaluator.plot_scatter())
        st.plotly_chart(evaluator.plot_residuals())
        st.plotly_chart(evaluator.plot_feature_importances())
        st.plotly_chart(evaluator.plot_shap_values())
    