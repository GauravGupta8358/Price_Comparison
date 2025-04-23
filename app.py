import serpapi
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def compare(mac_name):
    params = {
        "engine": "google_shopping",
        "q": "mac_name",
        "api_key": "75754787bcc169f9c544d5e5c28fcecb179b4dc329c9dbcbaa91e9b38ea2442f",
        "gl":"in"
    }
    search = serpapi.GoogleSearch(params)
    results = search.get_dict()
    shopping_results = results['shopping_results']
    return shopping_results

c1,c2 = st.columns(2)
c1.image('macbook.png',width = 250)
c2.header('Macbook Price Comparison System ')

# """--------------------------------------------------"""
st.sidebar.title('Enter name of model:')
mac_name = st.sidebar.text_input("Enter name 👇:")
number = st.sidebar.text_input("Enter numbers of options 👇:")
mac = []
mac_price = []
if mac_name is not None:
    if st.sidebar.button("price compare"):
        shopping_results = compare(mac_name)
        print(number)
        lowest_price = float((shopping_results[0].get("price"))[1:].replace(",", ""))
        print(lowest_price)
        lowest_price_index = 0
        st.sidebar.image(shopping_results[3].get('thumbnail'))
        for i in range(int(number)):
            current_price = float(shopping_results[i].get('price')[1:].replace(",",""))
            mac.append(shopping_results[i].get('source'))
            mac_price.append(float((shopping_results[i].get("price"))[1:].replace(",","")))

            #--------------------------------------------------------------------------
            st.title(f'option{i+1}')
            c1,c2= st.columns(2)
            c1.write("Company:")
            c2.write(shopping_results[i].get('source'))

            c1.write("Title:")
            c2.write(shopping_results[i].get('title'))

            c1.write("Price:")
            c2.write(shopping_results[i].get('price'))

            url = shopping_results[i].get('product_link')
            c1.write("Buy Link:")
            c2.write("[link](%s)"%url)
            print(url)
            """----------------------------------------------------------------------------------------------------------"""
            if current_price < lowest_price:
                lowest_price = current_price
                lowest_price_index = i

       # Best options
        st.title('Best option')
        c1, c2 = st.columns(2)
        c1.write("Company:")
        c2.write(shopping_results[lowest_price_index].get('source'))

        c1.write("Title:")
        c2.write(shopping_results[lowest_price_index].get('title'))

        c1.write("Price:")
        c2.write(shopping_results[lowest_price_index].get('price'))

        url = shopping_results[lowest_price_index].get('Product_link')
        c1.write("Buy Link:")
        c2.write("[link](%s)"%url)

    # Graphs compare

    df = pd.DataFrame(mac_price,mac)
    st.title('Chart Comparison')
    st.bar_chart(df)

    fig,ax = plt.subplots()
    ax.pie(mac_price,labels = mac,shadow = True)
    ax.axis("equal")
    st.pyplot(fig)