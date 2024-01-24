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
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="neal.work",
        page_icon="👋",
        layout="wide",
        
    )


    # get query string param "page" from url
    page = st.query_params["page"] if "page" in st.query_params else "home"
    # confirm that query is not trying to change to any other folder except current one
    if "/" not in page:
      if page != "home":
          # attempt to read file from docs folder with the same name as page
          # if it doesn't exist, throw an error
          try:
              st.markdown(open(f"docs/{page}.md").read())
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
