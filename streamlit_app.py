import streamlit as st
from supabase import create_client

# Supabase に接続
supabase = create_client(st.secrets["supabase"]["url"], st.secrets["supabase"]["key"])

st.title("Todo List")

# Todo 追加
new_todo = st.text_input("新しいTodo")
if st.button("追加") and new_todo:
    supabase.table("todos").insert({"title": new_todo}).execute()
    st.success("追加しました！")

# Todo 一覧取得
todos = supabase.table("todos").select("*").execute().data

# Todo 表示（タイトルと完了チェックボックス）
for todo in todos:
    completed = st.checkbox(todo["title"], value=todo["completed"], key=todo["id"])
    # 完了状態の更新
    if completed != todo["completed"]:
        supabase.table("todos").update({"completed": completed}).eq("id", todo["id"]).execute()
