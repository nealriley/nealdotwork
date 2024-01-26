# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import streamlit.components.v1 as components
import markdown
from streamlit.logger import get_logger
import ollama

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="neal.work",
        page_icon="random",
        layout="wide",
    )
    # Store the generate prompt in a browser cache
    if "generated_text" not in st.session_state:
        st.session_state["generated_text"] = ""

    hide_decoration_bar_style = '''
        <style>
            header {visibility: hidden;}
        </style>
    '''
    st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)


    # get query string param "page" from url
    page = st.query_params["page"] if "page" in st.query_params else "home"
    # confirm that query is not trying to change to any other folder except current one
    if "/" not in page:
      if page != "home":
          # attempt to read file from docs folder with the same name as page
          # if it doesn't exist, throw an error
          try:
              markdown_doc=open(f"docs/{page}.md").read()
              md = markdown.Markdown(extensions=['meta'])
              converted=md.convert(markdown_doc) 
              if "title" in md.Meta:
                  st.title(md.Meta["title"][0])          
                  st.markdown(converted, unsafe_allow_html=True)
              if "prompt" in md.Meta and st.session_state["generated_text"] != "":
                  print("prompting with " + md.Meta["prompt"][0])
                  response = ollama.chat(model='llama2', messages=[
                  {
                      'role': 'user',
                      'content': md.Meta["prompt"][0],
                      'stream': False                      
                  },
                  ])
                  print(response["message"])
                  st.session_state["generated_text"] = response['message']['content']
              st.markdown(st.session_state["generated_text"], unsafe_allow_html=True)
          except FileNotFoundError:
              st.error(f"404 - Page `{page}` not found")
          # Convert the page to an int, increment by one, and load the current url with a new query param (the new page id)
          # This will cause the page to reload with the new page id
          page_id = int(page) + 1
          st.markdown(f"""
            <a href=/?page={page_id} target = "_self"> 
                Next
            </a>
          """, unsafe_allow_html=True)

      else:
          st.markdown(f""" ## Welcome            
""")

if __name__ == "__main__":
    run()
