import streamlit as st

st.write("Hello World")
st.write("-----")

"""
# My first app
Here's our first attempt at using data to create a table:
"""
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write("이것도 가능하고")
df

# st.write("이것도 가능하고")
# st.write(df)

# st.write("이것도 가능하고")
# st.write(pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# }))

st.write("-----")
st.write("st.dataframe() 및 st.table() 과 같은 다른 데이터 특정 함수를 표시하는 데 사용할 수도 있습니다")

import numpy as np
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

st.write("하이라이트 표시 가능합니다.")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.dataframe(dataframe.style.highlight_max(axis=0))

st.write("st.table()로 표를 나타낼 수 있습니다.")
st.table(dataframe)

st.write("-----")
st.write("st.line_chart()를 사용하여 앱에 꺾은선형 차트를 쉽게 추가할 수 있습니다.")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

st.write("-----")
st.write("st.map()을 사용하면 지도에 데이터 포인트를 표시할 수 있습니다.")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)

st.write("-----")
st.write("st.slider(), st.button() 또는 st.selectbox()와 같은 위젯을 추가할 수 있습니다.")
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name

st.write("-----")
st.write("st.checkbox()는 확인란의 한 가지 사용 사례는 특정 차트 또는 섹션을 숨기거나 표시하는 것")
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])
    chart_data


st.write("-----")
st.write("원하는 옵션을 작성하거나 배열 또는 데이터 프레임을 전달할 수 있습니다.")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

st.write("-----")
st.write("st.sidebar를 사용하여 왼쪽 패널 사이드바에서 위젯을 쉽게 구성할 수 있습니다.")
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


st.write("-----")
st.write("st.progress()를 사용하여 실시간으로 상태를 표시할 수 있습니다.")

import time
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'