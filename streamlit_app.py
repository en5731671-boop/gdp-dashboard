import streamlit as st

st.title("シンプル Todo リスト")

# Todo をセッションに保存
if "todos" not in st.session_state:
    st.session_state.todos = []

# Todo 追加
new_todo = st.text_input("新しいTodo")
if st.button("追加") and new_todo:
    st.session_state.todos.append({"title": new_todo, "completed": False})
    new_todo = ""  # 入力欄を空に

# Todo 表示
for i, todo in enumerate(st.session_state.todos):
    col1, col2, col3 = st.columns([0.1, 0.7, 0.2])
    
    # 完了チェックボックス
    checked = col1.checkbox("", value=todo["completed"], key=f"chk{i}")
    st.session_state.todos[i]["completed"] = checked
    
    # タイトル表示
    col2.write(todo["title"])
    
    # 削除ボタン
    if col3.button("削除", key=f"del{i}"):
        st.session_state.todos.pop(i)
        break  # pop したらループを抜ける
