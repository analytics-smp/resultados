import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="MKT/Members Results", page_icon="📱", layout="centered", initial_sidebar_state="auto")

#Title
st.markdown("<h1 style='text-align: center;'>Resultados de Enero</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>SMP Data Analytics</h2>", unsafe_allow_html=True)
st.markdown("---")


#Analysis Select Box
st.markdown(
    """
    <div style="text-align: center;">
        <br>
        <br>
        <h3>Metricas y KPIs de Enero 2025 📊</h3>
    </div>
    """, 
    unsafe_allow_html=True
)
add_selectbox = st.selectbox(
    'Categoria',
    ('Marketing', 'Members')
)

match add_selectbox:
    case 'Marketing':

        #Analysis Select Box
        add_selectbox = st.selectbox(
            'Categoria',
            ('Generales', 'IG', 'YT', 'FB', 'Tiktok', 'LinkedIn')
        )

        match add_selectbox:
            case 'Generales':

                col1, col2 = st.columns(2)
                col3, col4 = st.columns(2)

                with col1:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Views</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format("{:,}".format(int(17438552))), unsafe_allow_html=True)

                with col2:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Reach</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format("{:,}".format(int(7352763))), unsafe_allow_html=True)

                with col3:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Engagement</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format("{:,}".format(int(85487))), unsafe_allow_html=True)

                
                with col4:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Followers</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format("{:,}".format(int(1800969))), unsafe_allow_html=True)

                st.markdown("---")

                # Display the diagram in Streamlit
                st.markdown(
                    """
                    <div style="text-align: center;">
                        <br>
                        <br>
                        <h3>Best Practices Enero 2025:</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # Show the image
                st.image('static/mejorespracticasenero.png', use_container_width=True)

            case 'IG':
                ig_jan = dict.fromkeys(['Views', 'Reach', 'Engagement', 'Followers'])
                ig_jan_kpis = ...

                col1, col2 = st.columns(2)
                col3, col4 = st.columns(2)
                col5 = st.columns(1)

                with col1:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Views</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format("{:,}".format(int(2798945))), unsafe_allow_html=True)

                with col2:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Reach</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format("{:,}".format(int(893876))), unsafe_allow_html=True)

                with col3:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Engagement</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format("{:,}".format(int(27954))), unsafe_allow_html=True)

                
                with col4:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Followers</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format("{:,}".format(int(391958))), unsafe_allow_html=True)

                with col5[0]:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Average Engagement Rate</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format(str("3.13%")), unsafe_allow_html=True)

                st.markdown("---")

                st.header("Mejor Contenido de Enero:")
                st.subheader("El secreto del sabor irresistible es la magia de la reacción de Maillard.🔥")
                st.subheader("226,668 views")
                st.subheader("153,879 reach")
                st.subheader("9,184 engagement")
                st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                st.image("static/reaccion_maillard.png", use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)

            case 'YT':
                col1, col2 = st.columns(2)
                col3, col4 = st.columns(2)
                col5 = st.columns(1)
                col6 = st.columns(1)

                with col1:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Views</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format("{:,}".format(int(209110))), unsafe_allow_html=True)

                with col2:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Revenue</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format(format(str('$3758.53'))), unsafe_allow_html=True)

                with col3:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Engagement</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format("{:,}".format(int(3093))), unsafe_allow_html=True)

                with col4:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Followers</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format("{:,}".format(int(136400))), unsafe_allow_html=True)

                with col5[0]:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Reach</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format("{:,}".format(int(123234))), unsafe_allow_html=True)

                with col6[0]:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Average Engagement Rate</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format(str('2.51%')), unsafe_allow_html=True)

                st.markdown("---")

                st.header("Mejor Contenido de Enero:")
                st.subheader("Carbon vs Gas.🔥")
                st.subheader("47,269 views")
                st.subheader("42,361 reach")
                st.subheader("129 engagement")
                st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                st.image("static/carbonvsgas.png", use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)

            case 'FB':
                col1, col2 = st.columns(2)
                col3, col4 = st.columns(2)
                col5 = st.columns(1)

                with col1:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Views</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format("{:,}".format(int(13836257))), unsafe_allow_html=True)

                with col2:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Reach</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format("{:,}".format(int(6335653))), unsafe_allow_html=True)

                with col3:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Engagement</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format("{:,}".format(int(36104))), unsafe_allow_html=True)

                
                with col4:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Followers</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format(str("1.2M")), unsafe_allow_html=True)

                with col5[0]:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Average Engagement Rate</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format(str("0.57%")), unsafe_allow_html=True)

                    st.header("Mejor Contenido de Enero:")
                    st.subheader("Ribeye completo, raza. Aquí nada se desperdicia🔥🥩")
                    st.subheader("171,699 views")
                    st.subheader("147,983 reach")
                    st.subheader("3,299 engagement")
                    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                    st.image("static/nadasedesperdicia.png", use_container_width=True)
                    st.markdown("</div>", unsafe_allow_html=True)

            case 'Tiktok':
                col1, col2 = st.columns(2)
                col3, col4 = st.columns(2)

                with col1:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Views</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format("{:,}".format(int(589000))), unsafe_allow_html=True)

                with col2:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Followers</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format("{:,}".format(int(270100))), unsafe_allow_html=True)

                with col3:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Engagement</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format("{:,}".format(int(18179))), unsafe_allow_html=True)

                
                with col4:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Average Engagement Rate</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format(str("6.73%")), unsafe_allow_html=True)

            case 'LinkedIn':
                col1, col2 = st.columns(2)
                col3 = st.columns(1)

                with col1:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Impressions</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format("{:,}".format(int(5240))), unsafe_allow_html=True)

                with col2:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Engagement</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format("{:,}".format(int(157))), unsafe_allow_html=True)
                
                with col3[0]:
                    st.markdown("""
                        <div style='border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; height: 150px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 20px;'>
                            <h3 style='text-align: center; color: #333;'>Followers</h3>
                            <p style='font-size: 24px; font-weight: bold; color: #333; text-align: center;'>{}</p>
                        </div>
                    """.format(str("2,311")), unsafe_allow_html=True)

    case 'Members':

        # Load data
        active_members = pd.read_csv(r'members/members_analysis(activemembers).csv')

        # Ensure proper column parsing
        active_members.set_index(active_members.columns[0], inplace=True)  # Set first column as index
        active_members = active_members.T  # Transpose to have dates as x-axis

        # Extract data
        dates = active_members.index.tolist()  # X-axis labels
        percentages = active_members['%'].tolist()  # Line chart values
        total_members = active_members['Total Members'].tolist()  # Bar chart values

        # Create figure
        fig = go.Figure()

        # Add bar chart for total members with data labels
        fig.add_trace(go.Bar(
            x=dates,
            y=total_members,
            name='Total Members',
            yaxis='y1',
            marker_color='light blue',
            text=[f'{int(t)}' for t in total_members],  # Round total members
            textposition='outside',  # Position labels outside bars
            textfont=dict(color='black')
        ))

        # Add line chart for percentages with data labels
        fig.add_trace(go.Scatter(
            x=dates,
            y=percentages,
            name='%',
            yaxis='y2',
            mode='lines+markers+text',  # Include text labels
            marker_color='red',
            text=[f'{p:.2%}' for p in percentages],  # Format percentage labels
            textposition='top center',  # Position labels above markers
            textfont=dict(size = 14,color='black')
        ))

        # Update layout
        fig.update_layout(
            title='Active Members vs Total Members Over Time',
            xaxis=dict(title='Month'),
            yaxis=dict(title='Total Members', side='left', showgrid=False),
            yaxis2=dict(title='%', overlaying='y', side='right', showgrid=False),
            legend=dict(x=0.1, y=1.1, orientation='h'),
            barmode='group',
            width=1500,  # Increase width
            height=500,  # Increase height
            margin=dict(t=60, b=80, l=40, r=40)  # Adjusting margins (top, bottom, left, right)

        )

        # Display in Streamlit
        st.markdown(
            "_En enero de 2025 tuvimos 3 miembros nuevos, pasando de 112 a 115, con una participación de 37 miembros, lo que da un 32% de actividad._")
        st.plotly_chart(fig)
        st.markdown("---")

        #Cumulative Members Proportion
        cum_members = pd.read_csv(r'members/members_analysis(membercount_fixed).csv')

        # Rename the 'Mes' column to 'Month'
        cum_members.rename(columns={'Mes': 'Month'}, inplace=True)

        # Calculate totals per month
        cum_members['Total'] = cum_members['Choice'] + cum_members['Prime'] + cum_members['Black']

        # Create figure
        fig = go.Figure()

        # Add stacked bars for each category
        fig.add_trace(go.Bar(
            x=cum_members["Month"],
            y=cum_members["Choice"],
            name='Choice',
            marker_color='red',
            text=cum_members["Choice"],
            textposition='inside',
            textfont=dict(size=14, color='white')  # Adjust font size and color
        ))

        fig.add_trace(go.Bar(
            x=cum_members["Month"],
            y=cum_members["Prime"],
            name='Prime',
            marker_color='blue',
            text=cum_members["Prime"],
            textposition='inside',
            textfont=dict(size=14, color='white')  # Adjust font size and color
        ))

        fig.add_trace(go.Bar(
            x=cum_members["Month"],
            y=cum_members["Black"],
            name='Black',
            marker_color='black',
            text=cum_members["Black"],
            textposition='inside',
            textfont=dict(size=14, color='white')  # Adjust font size and color
        ))

        # Add totals at the top of each bar
        fig.add_trace(go.Scatter(
            x=cum_members["Month"],
            y=cum_members["Total"],
            mode='text',
            text=cum_members["Total"].apply(lambda x: f'{int(x)}'),
            textposition='top center',  # Position text at the top of each bar
            showlegend=False,
            textfont=dict(size=14, color='black')  # Adjust font size and color for total
        ))

        # Update layout for stacked bar chart
        fig.update_layout(
            title='Members by Category Per Month',
            xaxis=dict(title='Month'),
            yaxis=dict(title='Number of Members'),
            barmode='stack',
            legend=dict(x=0.1, y=1.1, orientation='h'),
            width=1200,  # Increase width
            height=650,  # Increase height
            margin = dict(t=90, b=100, l=100, r=100)  # Adjusting margins (top, bottom, left, right)
        )

        # Display in Streamlit
        st.markdown("_En enero se obtuvieron 1 Choice y 2 Black, dando un total de 115 miembros hasta el día de hoy._")
        st.plotly_chart(fig)
        st.markdown("---")

        #Net Sales Through Time
        net_sales = pd.read_csv(r'members/members_analysis(net sales thru time).csv')
        net_sales.rename(columns={'month': 'Month'}, inplace=True)
        net_sales.rename(columns={'net sales': 'Net Sales'}, inplace=True)
        net_sales = net_sales[net_sales['Month'].astype(str).str.contains('24|25', regex=True)]
        net_sales['Net Sales'] = net_sales['Net Sales'].replace({'\$': '', ',': ''}, regex=True).astype(float)

        # Calculate the average line
        average_value = 197894.29

        # Create the figure
        fig = go.Figure()

        # Add bars for each month
        fig.add_trace(go.Bar(
            x=net_sales["Month"],
            y=net_sales["Net Sales"],
            name='Net Sales',
            marker_color='light blue',
            text=[f"${x:,.2f}" for x in net_sales["Net Sales"]],
            textposition='outside',
            textfont=dict(size=10, color='black'),  # Adjust font size and color for total
            cliponaxis=False

        ))

        # Add a horizontal line for the average
        fig.add_trace(go.Scatter(
            x=net_sales["Month"],
            y=[average_value] * len(net_sales),
            mode='lines',
            name='Average',
            line=dict(color='red', dash='dash'),
            text=[f"Average: ${average_value:,.2f}"] * len(net_sales),
            textposition='bottom center'
        ))

        # Update layout
        fig.update_layout(
            title="Net Sales per Month with Average Line",
            xaxis=dict(title="Month"),
            yaxis=dict(title="Net Sales (in $)", tickprefix="$"),
            barmode='group',
            legend=dict(x=0.1, y=1.1, orientation='h'),
            showlegend=True,
            width=2000,  # Increase width
            height=600,  # Increase height
            margin=dict(t=110, b=100, l=100, r=100),  # Adjusting margins (top, bottom, left, right)
            uniformtext=dict(minsize=10, mode='show')
        )

        # Display the chart in Streamlit
        st.markdown(
            "_En enero, las ventas netas generadas por 37 miembros activos con 212 transacciones fueron de $216,207.43. SMP Members estuvo por encima de las ventas netas promedio de los miembros._")
        st.plotly_chart(fig)
        st.markdown("---")

        #Average Ticket
        avg_ticket = pd.read_csv(r'members/members_analysis(ticket).csv', index_col=0)

        # Extract relevant rows for ticket averages and standard deviations
        ticket_avg = avg_ticket.loc['ticket avg'].values
        stdev = avg_ticket.loc['stdev'].values

        # Extract months from the column headers (excluding 'Index')
        months = avg_ticket.columns.tolist()

        # Filter months to only include those with '24' or '25' in the year part
        filtered_months = [month for month in months if '24' in month or '25' in month]

        ticket_avg_filtered = ticket_avg[months.index(filtered_months[0]):months.index(filtered_months[-1]) + 1]
        stdev_filtered = stdev[months.index(filtered_months[0]):months.index(filtered_months[-1]) + 1]

        # Create the figure
        fig = go.Figure()

        # Add bar trace for ticket averages
        fig.add_trace(go.Bar(
            x=filtered_months,
            y=ticket_avg_filtered,
            name='Ticket Average',
            marker_color='light blue',
            error_y=dict(
                type='data',  # Error bars are based on the 'stdev' values
                array=stdev_filtered,
                visible=True,
                thickness=1.5,  # Adjust the thickness of error bars
                width=5,  # Adjust the width of error bars
                color='red'
            ),
            text=[f"${val:.2f}" for val in ticket_avg_filtered],  # Format labels
            textposition='outside',  # Position the labels inside the bars
            texttemplate="%{text}",  # Use texttemplate toticket_avg[:len(filtered_months)]] avoid resizing
            insidetextanchor="start",
            textfont=dict(size=40, color='black'),  # Adjust font size and color for total
        ))

        # Update layout to make the chart look better
        fig.update_layout(
            title="Ticket Average with Standard Deviation Error Bars",
            xaxis=dict(title="Month", tickangle=45),  # Rotate month labels for better readability
            yaxis=dict(title="Ticket Average", tickprefix="$"),
            barmode='group',
            showlegend=True,
            legend=dict(
                orientation="h",  # Horizontal legend
                yanchor="bottom",
                y=1.0,  # Move legend above chart
                xanchor="center",
                x=0.5
            ),
            margin=dict(l=20, r=20, t=100, b=100),  # Increase bottom margin for labels
            autosize=True,  # Ensure the plot scales to fit the size of the labels
            height=600,  # Adjust height if needed
            width=2000,  # Increase width
        )

        st.markdown("_El ticket promedio en enero fue de $1,019.85._")
        st.markdown("_Los miembros gastan alrededor de $1,000 por compra._")
        st.markdown("_La desviación estándar es de $2,283.87._")
        st.markdown("_Hay tickets de hasta $2,200._")
        st.markdown("_La mayoría se mantiene cerca del promedio de $1,019._")

        st.plotly_chart(fig)
        st.markdown("---")

        member_sales_vendor = pd.read_csv(r'members/members_analysis(net sales per vendor time).csv')
        member_sales_vendor['Vendor'] = member_sales_vendor['Vendor'].str.strip()

        # Filter the relevant column for 'enero 25' (January 2025)
        member_sales_enero_25 = member_sales_vendor['enero 25']

        # Drop the row labeled 'Total' since we don't need it for the pie chart
        member_sales_vendor = member_sales_vendor[member_sales_vendor['Vendor'] != 'Total']

        # Define a color map for vendors, making "Big Green Egg" green
        color_map = {
            'Big Green Egg': 'green',  # Set 'Big Green Egg' to green
            'Grill Academy': 'lightblue',
            'Marca Propia': 'orange',
            'Victorinox': 'purple',
            'SMP MEMBERS': 'pink',
            'BLACKSTONE': 'red',
            'Lodge Cast Iron': 'brown',
            'Cinsa': 'gray',
            'New Era': 'yellow',
            'Lulo Gelato': 'lightgreen',
            'Proan': 'blue',
            'Stanley': 'lightcoral',
            'Weber': 'teal',
            'Kingsford': 'gold',
            'Franks': 'lightpink',
            'Royal Kitchen': 'lightyellow',
            'Grill Master': 'lightgreen',
            'Pines Cursos': 'lightcyan',
            'Asadores MTY': 'lavender'
        }

        # Create the pie chart
        fig = px.pie(
            member_sales_vendor,  # DataFrame to be used
            names='Vendor',  # Vendor names as labels
            values='enero 25',  # Sales values for Enero 25
            title="Sales per Vendor - Enero 25",
            labels={'Vendor': 'Vendor', 'enero 25': 'Sales ($)'},
            color = 'Vendor',
            color_discrete_map=color_map
        )

        # Show the chart in Streamlit
        st.markdown("_Grill Academy, Marca Propia y Big Green Egg (BGE) fueron los vendors con más ventas a miembros._")
        st.plotly_chart(fig)

        # Melt the DataFrame to have a 'Vendor' and 'Sales' columns for stacked bar chart
        member_sales_melted = member_sales_vendor.melt(id_vars=["Vendor"], var_name="Month", value_name="Sales")

        total_sales_per_month = member_sales_melted.groupby('Month')['Sales'].sum().reset_index()

        # Create the stacked bar chart with months on x-axis and vendors stacked in the y-axis
        fig = px.bar(
            member_sales_melted,
            x="Month",  # X-axis: Months
            y="Sales",  # Y-axis: Sales values
            color="Vendor",  # Stack the bars by 'Vendor'
            title="Sales per Month by Vendor",
            labels={'Sales': 'Sales ($)', 'Month': 'Month'},
            height=500,  # Adjust the height if needed
            barmode='stack',  # Ensure bars are stacked,
            color_discrete_map=color_map
        )

        # Add the total sales as text on top of the stacked bars
        for month in total_sales_per_month['Month']:
            total_sales = total_sales_per_month.loc[total_sales_per_month['Month'] == month, 'Sales'].values[0]

            # Ensure total_sales is a valid numeric value (float)
            if pd.notnull(total_sales) and isinstance(total_sales, (int, float)):
                fig.add_annotation(
                    x=month,  # Month as x coordinate
                    y=total_sales * 1.10,  # Place text slightly above the total sales
                    text=f"${total_sales:,.2f}",  # Format as currency
                    showarrow=False,
                    font=dict(size=12, color="black"),
                    align="center",
                    verticalalignment="bottom"
                )

        # Show the chart in Streamlit
        st.plotly_chart(fig)
        st.markdown("---")

        #Sales per Channel
        sales_channel = pd.read_csv(r'members/members_analysis(channel sales thru time).csv')

        # Clean the sales data: remove dollar signs and commas, then convert to numeric
        for column in sales_channel.columns[1:]:  # Skip the 'Channel' column
            sales_channel[column] = sales_channel[column].replace({'\$': '', ',': ''}, regex=True)
            sales_channel[column] = pd.to_numeric(sales_channel[column],
                                                  errors='coerce')  # Convert to numeric, forcing errors to NaN

        # Clean the sales data: remove dollar signs and commas, then convert to numeric
        sales_channel['enero 25'] = sales_channel['enero 25'].replace({'\$': '', ',': ''}, regex=True).astype(float)
        sales_channel.replace({' - ': None}, inplace=True)  # Replace ' - ' with None (which will be interpreted as NaN)

        # Create the pie chart for 'enero 25'
        fig = px.pie(
            sales_channel,  # DataFrame to be used
            names='Channel',  # Channel names as labels
            values='enero 25',  # Sales values for enero 25
            title="Sales per Channel - Enero 25",
            labels={'Channel': 'Channel', 'enero 25': 'Sales ($)'},
            color='Channel'  # Add colors for each channel
        )
        # Show the chart in Streamlit
        st.markdown("_Las ventas en línea acapararon la mayor proporción de ventas a miembros._")
        st.plotly_chart(fig)

        #Sales per channel through time
        # Melt the DataFrame to have a 'Month' and 'Sales' column for the stacked bar chart
        sales_melted = sales_channel.melt(id_vars=["Channel"], var_name="Month", value_name="Sales")

        # Create the stacked bar chart with months on x-axis and channels stacked in the y-axis
        fig = px.bar(
            sales_melted,  # DataFrame to be used
            x="Month",  # X-axis: Months
            y="Sales",  # Y-axis: Sales values
            color="Channel",  # Stack the bars by 'Channel'
            title="Sales per Channel by Month",
            labels={'Sales': 'Sales ($)', 'Month': 'Month'},
            height=500,  # Adjust the height if needed
            barmode='stack'  # Ensure bars are stacked
        )
        # Show the chart in Streamlit
        st.plotly_chart(fig)
        st.markdown("---")

        #SMP Cash
        df = pd.read_csv(r'members/members_analysis(smp cash).csv')

        # Create the figure
        fig = go.Figure()

        # Add bar chart for Redeemed
        fig.add_trace(go.Bar(
            x=df["Mes"],
            y=df["Redeemed"],
            name="Redeemed",
            marker_color="lightblue",
            text=df["Redeemed"],
            textposition="inside"
        ))

        # Add line chart for Total Sales (secondary y-axis)
        fig.add_trace(go.Scatter(
            x=df["Mes"],
            y=df["Total Sales"],
            name="Total Sales",
            mode="lines+markers+text",  # Ensure markers and text are included
            yaxis="y2",
            line=dict(color="red", width=3),
            marker=dict(size=8),
            text=[f"${x:,.2f}" for x in df["Total Sales"]],  # Add data labels for Total Sales
            textposition="bottom center",  # Position the labels above the markers
            textfont=dict(size=12, color="black")  # Adjust font size and color for Total Sales labels
        ))

        # Update layout
        fig.update_layout(
            title="SMP Cash Redeemed vs Grill Academy Member Total Sales",
            xaxis=dict(title="Month"),
            yaxis=dict(title="Redeemed"),
            yaxis2=dict(
                title="Total Sales ($)",
                overlaying="y",
                side="right",
                showgrid=False
            ),
            legend=dict(x=0.1, y=1.1, orientation="h"),
            width=1200,
            height=600
        )

        st.markdown(
            "_Se canjearon 11 códigos de descuento, los cuales incentivaron la generación de $48,699 en ventas de Grill Academy en Members._")
        st.plotly_chart(fig)

        #Webpage Usage
        # members_web = pd.read_csv(r"members/members_analysis(soyparrillero members web usage).csv")
        # soypa_web = pd.read_csv(r"members/members_analysis(soyparrillero mx web usage).csv")
