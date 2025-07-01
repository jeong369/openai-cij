import random
import streamlit as st

# def number_guessing_game():
#     print("1부터 100까지 숫자를 맞추는 게임입니다!")
#     target_number = random.randint(1, 100)
#     attempts = 0

#     while True:
#         try:
#             guess = int(input("숫자를 입력하세요: "))
#             attempts += 1

#             if guess < 1 or guess > 100:
#                 print("1부터 100 사이의 숫자를 입력해주세요.")
#             elif guess < target_number:
#                 print("더 큰 숫자입니다.")
#             elif guess > target_number:
#                 print("더 작은 숫자입니다.")
#             else:
#                 print(f"정답입니다! {attempts}번 만에 맞췄습니다.")
#                 break
#         except ValueError:
#             print("유효한 숫자를 입력해주세요.")

if __name__ == "__main__":
    def number_guessing_game_streamlit():
        st.title("1부터 100까지 숫자를 맞추는 게임!")

        if "target_number" not in st.session_state:
            st.session_state.target_number = random.randint(1, 100)
            st.session_state.attempts = 0

        guess = st.number_input("숫자를 입력하세요:", min_value=1, max_value=100, step=1)
        if st.button("확인"):
            st.session_state.attempts += 1
            if guess < st.session_state.target_number:
                st.write("더 큰 숫자입니다.")
            elif guess > st.session_state.target_number:
                st.write("더 작은 숫자입니다.")
            else:
                st.write(f"정답입니다! {st.session_state.attempts}번 만에 맞췄습니다.")
                st.session_state.target_number = random.randint(1, 100)
                st.session_state.attempts = 0

    number_guessing_game_streamlit()