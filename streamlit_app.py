import streamlit as st

# ページタイトル
st.title("シンプル Todo リスト")

# Todo を保存するセッション状態
if "todos" not in st.session_state:
    st.session_state.todos = []

# Todo を追加
new_todo = st.text_input("新しいTodo")
if st.button("追加") and new_todo:
    st.session_state.todos.append({"title": new_todo, "completed": False})
    st.experimental_rerun()  # 追加後に画面更新

# Todo 一覧表示
for i, todo in enumerate(st.session_state.todos):
    col1, col2, col3 = st.columns([0.1, 0.7, 0.2])
    
    # 完了チェックボックス
    completed = col1.checkbox("", value=todo["completed"], key=f"chk{i}")
    st.session_state.todos[i]["completed"] = completed
    
    # タイトル表示
    col2.write(todo["title"])
    
    # 削除ボタン
    if col3.button("削除", key=f"del{i}"):
        st.session_state.todos.pop(i)
        st.experimental_rerun()
