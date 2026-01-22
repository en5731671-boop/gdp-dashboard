import streamlit as st
from supabase import create_client, Client

# Supabase に接続
url = st.secrets["supabase"]["url"]
key = st.secrets["supabase"]["key"]
supabase: Client = create_client(url, key)

st.title("Todo List (Supabase)")

# Todo を追加
new_todo = st.text_input("新しいTodoを追加")
if st.button("追加") and new_todo:
    supabase.table("todos").insert({"title": new_todo}).execute()
    st.success(f"追加しました: {new_todo}")

# Todo を取得
todos = supabase.table("todos").select("*").execute().data

# Todo を表示
for todo in todos:
    col1, col2 = st.columns([0.1, 0.9])
    completed = col1.checkbox("", value=todo["completed"], key=todo["id"])
    st.write(todo["title"])
    
    # 完了状態の更新
    if completed != todo["completed"]:
        supabase.table("todos").update({"completed": completed}).eq("id", todo["id"]).execute()

# Todo の削除
for todo in todos:
    if st.button(f"削除 {todo['title']}", key=f"del{todo['id']}"):
        supabase.table("todos").delete().eq("id", todo["id"]).execute()
        st.experimental_rerun()
