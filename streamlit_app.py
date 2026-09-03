import streamlit as st


st.set_page_config(
    page_title="TripAdvisor Hotel Finder",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Streamlit oturum değişkenlerini başlangıçta oluştur
if "recommendations" not in st.session_state:
    st.session_state["recommendations"] = []

if "searched_destination" not in st.session_state:
    st.session_state["searched_destination"] = ""

if "searched_query" not in st.session_state:
    st.session_state["searched_query"] = ""


# TripAdvisor benzeri görünüm
st.markdown(
    """
    <style>
    .block-container {
        max-width: 1180px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }

    section[data-testid="stSidebar"] {
        border-right: 1px solid #e0e0e0;
    }

    .brand-title {
        font-size: 38px;
        font-weight: 800;
        color: #000000;
        margin-bottom: 4px;
    }

    .brand-title span {
        color: #00aa6c;
    }

    .brand-description {
        color: #545454;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .search-title {
        font-size: 30px;
        font-weight: 750;
        color: #000000;
        margin-bottom: 5px;
    }

    div[data-testid="stForm"] {
        border: 1px solid #dedede;
        border-radius: 18px;
        padding: 24px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.07);
    }

    .stTextArea textarea {
        border-radius: 14px;
        border: 2px solid #d6d6d6;
    }

    .stTextArea textarea:focus {
        border-color: #00aa6c;
        box-shadow: 0 0 0 1px #00aa6c;
    }

    .stFormSubmitButton > button {
        width: 100%;
        background-color: #00aa6c;
        color: white;
        border: none;
        border-radius: 24px;
        min-height: 48px;
        font-size: 16px;
        font-weight: 700;
    }

    .stFormSubmitButton > button:hover {
        background-color: #008f5b;
        color: white;
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Sol filtre paneli
with st.sidebar:
    st.header("🔎 Arama Filtreleri")

    destination = st.text_input(
        "Nereye gitmek istiyorsunuz?",
        placeholder="Örn: New York",
    )

    recommendation_count = st.slider(
        "Önerilecek otel sayısı",
        min_value=1,
        max_value=5,
        value=5,
    )

    minimum_rating = st.slider(
        "Minimum kullanıcı puanı",
        min_value=1.0,
        max_value=5.0,
        value=4.0,
        step=0.1,
    )

    hotel_classes = st.multiselect(
        "Otel sınıfı",
        options=[
            "3 yıldız",
            "4 yıldız",
            "5 yıldız",
        ],
        default=[
            "4 yıldız",
            "5 yıldız",
        ],
    )

    travel_type = st.selectbox(
        "Seyahat türü",
        options=[
            "Fark etmez",
            "Aile tatili",
            "Romantik tatil",
            "İş seyahati",
            "Tek başına seyahat",
        ],
    )

    st.divider()

    st.caption(
        "Bu ekran UI prototipidir. Gerçek öneri sistemi "
        "daha sonra bağlanacaktır."
    )


# Sayfa başlığı
st.markdown(
    """
    <div class="brand-title">
        🏨 TripAdvisor <span>Hotel Finder</span>
    </div>

    <div class="brand-description">
        Gerçek misafir yorumlarına göre size uygun otelleri keşfedin.
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div class="search-title">
        Mükemmel konaklama deneyimini bulun
    </div>
    """,
    unsafe_allow_html=True,
)

st.write(
    "Nasıl bir otel aradığınızı kendi kelimelerinizle anlatın."
)


# Ana arama formu
with st.form("hotel_search_form"):
    user_query = st.text_area(
        "Otel tercihiniz",
        placeholder=(
            "Örn: Merkezi konumda, sessiz, temiz ve "
            "çocuklu ailelere uygun bir otel arıyorum."
        ),
        height=130,
        label_visibility="collapsed",
    )

    search_button = st.form_submit_button(
        "🔍 Otelleri Bul"
    )


# Gerçek model bağlanana kadar kullanılacak örnek sonuçlar
mock_hotels = [
    {
        "name": "Central Park Boutique Hotel",
        "hotel_class": 5,
        "rating": 4.8,
        "match": 96,
        "reason": (
            "Merkezi konumu, sessiz odaları ve temizlik "
            "hakkındaki olumlu yorumlarıyla eşleşiyor."
        ),
        "review": (
            "The rooms were spotless, quiet and within "
            "walking distance of the city center."
        ),
    },
    {
        "name": "Riverside Family Hotel",
        "hotel_class": 4,
        "rating": 4.6,
        "match": 92,
        "reason": (
            "Aile dostu hizmetleri, geniş odaları ve sakin "
            "konumuyla tercihlerinize uyuyor."
        ),
        "review": (
            "A comfortable and peaceful hotel, especially "
            "suitable for families with children."
        ),
    },
    {
        "name": "City Garden Residence",
        "hotel_class": 4,
        "rating": 4.5,
        "match": 89,
        "reason": (
            "Ulaşım kolaylığı, temizliği ve güler yüzlü "
            "personeliyle öne çıkıyor."
        ),
        "review": (
            "Very clean, friendly staff and easy access "
            "to public transportation."
        ),
    },
    {
        "name": "Grand Avenue Hotel",
        "hotel_class": 5,
        "rating": 4.4,
        "match": 86,
        "reason": (
            "Merkezi konumu ve yüksek hizmet kalitesi "
            "nedeniyle öneriliyor."
        ),
        "review": (
            "Excellent location with professional service "
            "and comfortable rooms."
        ),
    },
    {
        "name": "Green Square Inn",
        "hotel_class": 3,
        "rating": 4.2,
        "match": 82,
        "reason": (
            "Uygun fiyatı, temiz odaları ve sakin çevresiyle "
            "iyi bir alternatif oluşturuyor."
        ),
        "review": (
            "A clean and quiet place offering good value "
            "for the price."
        ),
    },
]


# Form gönderildiğinde girişleri kontrol et
if search_button:
    if not destination.strip():
        st.warning(
            "Lütfen sol panelden gitmek istediğiniz yeri yazın."
        )
        st.session_state["recommendations"] = []

    elif not user_query.strip():
        st.warning(
            "Lütfen nasıl bir otel aradığınızı açıklayın."
        )
        st.session_state["recommendations"] = []

    else:
        selected_class_numbers = {
            int(hotel_class.split()[0])
            for hotel_class in hotel_classes
        }       

        filtered_hotels = [
        hotel
            for hotel in mock_hotels
                if hotel["rating"] >= minimum_rating
                and hotel["hotel_class"] in selected_class_numbers
        ]

        st.session_state["recommendations"] = filtered_hotels[
            :recommendation_count
            ]

        if not filtered_hotels:
            st.info(
                "Seçtiğiniz filtrelere uygun örnek otel bulunamadı. "
                "Minimum puanı veya otel sınıfını değiştirebilirsiniz."
            )
            st.session_state["searched_destination"] = destination
            st.session_state["searched_query"] = user_query


# Hazırlanan otelleri ekranda göster
recommendations = st.session_state.get(
    "recommendations",
    [],
)

if recommendations:
    searched_destination = st.session_state[
        "searched_destination"
    ]

    st.divider()

    st.subheader(
        f"🏨 {searched_destination} için önerilen oteller"
    )

    st.caption(
        "Sonuçlar şu anda prototip verilerle gösterilmektedir."
    )

    for index, hotel in enumerate(
        recommendations,
        start=1,
    ):
        with st.container(border=True):
            name_column, rating_column = st.columns(
                [4, 1]
            )

            with name_column:
                st.subheader(
                    f"{index}. {hotel['name']}"
                )

                st.write(
                    f"📍 {searched_destination} · "
                    f"{hotel['hotel_class']} yıldızlı otel"
                )

            with rating_column:
                st.metric(
                    "Kullanıcı puanı",
                    f"{hotel['rating']:.1f}/5",
                )

            filled_circles = "●" * round(
                hotel["rating"]
            )

            st.markdown(
                f"""
                <span style="
                    color:#00AA6C;
                    font-size:22px;
                    letter-spacing:3px;
                ">
                    {filled_circles}
                </span>
                """,
                unsafe_allow_html=True,
            )

            st.progress(
                hotel["match"] / 100,
                text=(
                    f"%{hotel['match']} tercih uyumu"
                ),
            )

            st.write(
                f"**Neden önerildi?** "
                f"{hotel['reason']}"
            )

            with st.expander(
                "Eşleşen kullanıcı yorumunu göster"
            ):
                st.markdown(
                    f"> “{hotel['review']}”"
                )