import streamlit as st

st.header('本週晚餐訂購')

st.subheader('請勾選有興趣的餐點')

col1, col2 = st.columns(2)

with col1:

    st.markdown('#### 是否訂購?')

    st.checkbox('Yes, 民以食為天')
    st.checkbox('No, 我要成仙')

    food = st.radio('Pick one',['中式','西式','日式'])
    drink = st.multiselect('飲料',['錫蘭紅茶','台灣碧螺春','義大利瑪奇朵','富士蘋果汁'])
    ice = st.slider('冰量',0,50,100)
    sugar = st.slider('糖量',0,100)
    
with col2:

    text1 = st.text_input('姓名') 
    d = st.date_input('訂購日期')
    t = st.time_input('領餐時間')
    text2 = st.text_area('備註')
    
    st.markdown('##### 請下載菜單，勾選並回傳')

    with open ("menu.csv","rb") as file:
        btn= st.download_button(
            label = "Download menu",
            data = file,
            file_name = "menu.csv",
            mime = 'csv',   #原本給老師的作業沒加入
            
        )
        
    data = st.file_uploader('Upload the menu' ,type = ['csv'])
    
    
if st.button('Click me'):
    st.write(f'晚餐 = {food}')
    st.write(f'飲料 = {drink}')
    st.write(f'冰量 = {ice}')
    st.write(f'糖量 = {sugar}')
    st.write(f'姓名 = {text1}')   
    st.write(f'date = {d}')
    st.write(f'time = {t}')
    st.write(f'備註 = {text2}')
    
else: 
    
    st.write('請按一下,謝謝!')







