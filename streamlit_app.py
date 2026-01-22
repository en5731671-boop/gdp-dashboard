import streamlit as st
from datetime import date

st.title(" Todo リスト")

# セッションにタスクを保存
if "todos" not in st.session_state:
    st.session_state.todos = []

# 新しいタスク入力
with st.form("new_task"):
    title = st.text_input("タスク名")
    deadline = st.date_input("締切日", value=date.today())
    priority = st.selectbox("優先度", ["5", "4", "3","2","1"])
    category = st.selectbox("カテゴリ", ["授業", "課題", "バイト", "その他"])
    submitted = st.form_submit_button("追加")
    
    if submitted and title:
        st.session_state.todos.append({
            "title": title,
            "deadline": deadline,
            "priority": priority,
            "category": category,
            "completed": False
        })

# Todo 一覧表示（期限順）
todos_sorted = sorted(st.session_state.todos, key=lambda x: x["deadline"])

for i, todo in enumerate(todos_sorted):
    # 色分け: 高→赤, 中→オレンジ, 低→緑
    color = {"5": "red", "4": "orange", "3": "yellow","2": "green","1": "blue"}[todo["priority"]]
    
    col1, col2, col3, col4, col5 = st.columns([0.05, 0.4, 0.15, 0.2, 0.1])
    
    # 完了チェック
    checked = col1.checkbox("", value=todo["completed"], key=f"chk{i}")
    st.session_state.todos[i]["completed"] = checked
    
    # タスク名 + カテゴリ
    col2.markdown(f"**{todo['title']}**  ({todo['category']})")
    
    # 締切日
    col3.write(todo["deadline"].strftime("%Y-%m-%d"))
    
    # 優先度
    col4.markdown(f"<span style='color:{color}'>{todo['priority']}</span>", unsafe_allow_html=True)
    
    # 削除ボタン
    if col5.button("削除", key=f"del{i}"):
        st.session_state.todos.pop(i)
        break
