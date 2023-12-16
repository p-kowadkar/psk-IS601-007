<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 API Project</td></tr>
<tr><td> <em>Student: </em> Pranav Kowadkar (psk)</td></tr>
<tr><td> <em>Generated: </em> 12/16/2023 12:18:56 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-2-api-project/grade/psk" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> API Details </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Which API did you choose?</td></tr>
<tr><td> <em>Response:</em> <p>I have used Anime_DB api:&nbsp;<a href="https://rapidapi.com/brian.rofiq/api/anime-db/discussions">https://rapidapi.com/brian.rofiq/api/anime-db</a>.<div>Direct documentation for the above API is not<br>available on the given link, however, apart from professor&#39;s notes, I followed the<br>below documentation:<br><a href="https://medium.com/analytics-vidhya/creating-anime-database-with-web-scraping-hand-on-tutorial-6f90e2174be1">Creating Anime Database With Web Scraping-Hand on Tutorial | by Tejas<br>Haritsa V K | Analytics Vidhya | Medium</a></div><div><div><br><div><br></div></div></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Which endpoints will be used?</td></tr>
<tr><td> <em>Response:</em> <div><span style="font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre; background-color: rgb(31, 31, 31); color:<br>rgb(206, 145, 120);">/list, /login, /logout, /profile, /fetch</span></div><span style="font-family: Consolas, &quot;Courier New&quot;, monospace; white-space:<br>pre; background-color: rgb(31, 31, 31); color: rgb(206, 145, 120);">title, </span><span style="font-family: Consolas, &quot;Courier<br>New&quot;, monospace; white-space: pre; background-color: rgb(31, 31, 31); color: rgb(206, 145, 120);">alternative_titles, </span><span<br>style="font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre; background-color: rgb(31, 31, 31); color: rgb(206,<br>145, 120);">genres, </span><span style="font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre; background-color: rgb(31, 31,<br>31); color: rgb(206, 145, 120);">status, </span><span style="font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre;<br>background-color: rgb(31, 31, 31); color: rgb(206, 145, 120);">episodes, </span><span style="font-family: Consolas, &quot;Courier New&quot;,<br>monospace; white-space: pre; background-color: rgb(31, 31, 31); color: rgb(206, 145, 120);">anime_type, </span><span style="font-family:<br>Consolas, &quot;Courier New&quot;, monospace; white-space: pre; background-color: rgb(31, 31, 31); color: rgb(206, 145,<br>120);">ranking</span><br><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> What pieces of data will be used in your app?</td></tr>
<tr><td> <em>Response:</em> <div style="color: rgb(204, 204, 204); background-color: rgb(31, 31, 31); font-family: Consolas, &quot;Courier New&quot;,<br>monospace; line-height: 19px; white-space: pre;"><div><span style="background-color: rgb(29, 29, 29); color: rgb(255, 255, 255);<br>font-family: Roboto, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; white-space: normal;">Title: Used for identification,<br>search, and linking to anime entries.</span><br></div><div><div style="color: rgb(255, 255, 255); font-family: Roboto, -apple-system,<br>&quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; white-space: normal; background-color: rgb(29, 29, 29);">Alternative Titles: For<br>cross-referencing and matching anime with different names.</div><div style="color: rgb(255, 255, 255); font-family: Roboto,<br>-apple-system, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; white-space: normal; background-color: rgb(29, 29, 29);">Genres: Querying<br>for recommendations, filtering content, and personalization.</div><div style="color: rgb(255, 255, 255); font-family: Roboto, -apple-system,<br>&quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; white-space: normal; background-color: rgb(29, 29, 29);">Status: Filtering available<br>anime (ongoing, finished) and tracking progress.</div><div style="color: rgb(255, 255, 255); font-family: Roboto, -apple-system,<br>&quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; white-space: normal; background-color: rgb(29, 29, 29);">Episodes: Displaying information,<br>progress, and tracking watched/unwatched episodes.</div><div style="color: rgb(255, 255, 255); font-family: Roboto, -apple-system, &quot;Helvetica<br>Neue&quot;, Helvetica, Arial, sans-serif; white-space: normal; background-color: rgb(29, 29, 29);">Anime Type: Categorization for<br>browsing/sorting (TV series, movies, specials).</div><div style="color: rgb(255, 255, 255); font-family: Roboto, -apple-system, &quot;Helvetica<br>Neue&quot;, Helvetica, Arial, sans-serif; white-space: normal; background-color: rgb(29, 29, 29);">Ranking: Displaying popularity, highlighting<br>highly-rated anime, and potentially powering recommendations.</div></div></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> How will you use the mapped data?</td></tr>
<tr><td> <em>Response:</em> <p>The objective of mapped data is to enable users to see list of<br>anime, and add to their watchlist.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Create Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show the create page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-16T01.59.33image.png.webp?alt=media&token=73dbd9b6-0ce3-43b3-baf5-effcd1ed98c1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data filled before submission.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-16T02.01.05image.png.webp?alt=media&token=bc83c605-d4e0-42f0-ab89-aa725a73f0ac"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successfully inserted data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-16T02.02.08image.png.webp?alt=media&token=8bded9f9-1bc5-4877-bab2-805d8f848eb7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Duplicate record<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-16T02.03.17image.png.webp?alt=media&token=d5fbd430-433f-4e37-8328-fe12352e8c69"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid entry<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-16T02.06.17image.png.webp?alt=media&token=52cfcf43-3d72-4c9e-a4f9-e2778c332956"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show the new data in the database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-16T02.07.15image.png.webp?alt=media&token=84bc2154-239d-4054-8861-321ecc4a27c8"/></td></tr>
<tr><td> <em>Caption:</em> <p>naruto added at the very end<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/p-kowadkar/psk-IS601-007/pull/28">https://github.com/p-kowadkar/psk-IS601-007/pull/28</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> List Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page that lists the application entities (both API and custom)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-16T05.02.14image.png.webp?alt=media&token=9218d063-7402-4c03-833e-1bc1ac92f421"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data fetched from API<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-16T05.03.20image.png.webp?alt=media&token=a69901b4-c781-4410-b2ec-28feec12624c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Last two data are custom data.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/p-kowadkar/psk-IS601-007/pull/28">https://github.com/p-kowadkar/psk-IS601-007/pull/28</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> View Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page showing a single entity with more details shown</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-16T05.04.37image.png.webp?alt=media&token=1b843e4a-f7ae-41a8-b2f1-4837d6f6a73d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Entity details fetched<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-16T05.05.59image.png.webp?alt=media&token=1d192e9e-5893-4b6f-bda2-a5986583a679"/></td></tr>
<tr><td> <em>Caption:</em> <p>Searched with name<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/p-kowadkar/psk-IS601-007/pull/28">https://github.com/p-kowadkar/psk-IS601-007/pull/28</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page to edit a single entity</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-16T05.06.26image.png.webp?alt=media&token=bd4a9dca-64f2-4a6d-a299-73f17e79d15c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Entity fetched by name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-16T05.08.22image.png.webp?alt=media&token=6c96684b-deff-4809-be54-b5117339a12c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Entity edit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-16T05.09.36image.png.webp?alt=media&token=32170356-0ab6-42b7-b903-c43335d12327"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-16T05.10.06image.png.webp?alt=media&token=63012eae-30f2-4b79-8044-468f240e8b67"/></td></tr>
<tr><td> <em>Caption:</em> <p>After (see second reading)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/p-kowadkar/psk-IS601-007/pull/28">https://github.com/p-kowadkar/psk-IS601-007/pull/28</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a route for deletion logic</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-16T05.11.12image.png.webp?alt=media&token=4625cd8c-9990-46b6-84f2-9f5a02de9219"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting (One piece)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-16T05.11.59image.png.webp?alt=media&token=ee16c1c5-eef7-4608-9b66-67a765a70a16"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deleting <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-16T05.12.30image.png.webp?alt=media&token=77b97279-b45b-4e32-9745-e56053a66caa"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before (See second from the last)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-16T05.13.29image.png.webp?alt=media&token=56f04a0a-3551-4327-8f33-8722a2f69bd4"/></td></tr>
<tr><td> <em>Caption:</em> <p>After (One Piece is deleted)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/p-kowadkar/psk-IS601-007/pull/28">https://github.com/p-kowadkar/psk-IS601-007/pull/28</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> API Data Loading </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show information related to API data loading</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-16T05.14.18image.png.webp?alt=media&token=ec6c790c-7c47-4147-ba0e-7f61af21c6af"/></td></tr>
<tr><td> <em>Caption:</em> <p>Feth code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-16T05.16.11image.png.webp?alt=media&token=7bd22ce8-c51e-4493-b9f2-7c162cc76d5d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add method (explaining duplicates while adding)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe the process</td></tr>
<tr><td> <em>Response:</em> <div>1. The user triggers data loading by accessing the "/fetch" route in the<br>Flask app.</div><div>2. The app communicates with an external Anime API using the `Anime`<br>class, retrieves data, and transforms it.</div><div>3. The transformed data is then inserted into<br>the database table "IS601_Anime" using SQL queries with a mechanism to handle duplicates<br>and update existing records.</div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/p-kowadkar/psk-IS601-007/pull/29">https://github.com/p-kowadkar/psk-IS601-007/pull/29</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>I had difficulty fetching the data, and once I was finally able to<br>fetch the data, it was really difficult to get the CRUD operations working!<br>I have learnt end to end problem solving during this!<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-psk-prod-1dc8f6f2f85b.herokuapp.com/login">https://is601-psk-prod-1dc8f6f2f85b.herokuapp.com/login</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Include Screenshots from Wakatime</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fpsk%2F2023-12-16T04.40.13image.png.webp?alt=media&token=52d3cede-eb9e-42d9-a887-cc35d2521145"/></td></tr>
<tr><td> <em>Caption:</em> <p>Link to the above: <a href="https://wakatime.com/@a6d70ece-69cf-4855-a63d-da6f79143fbd/projects/pwhmecwvqf?start=2023-12-09&end=2023-12-15">https://wakatime.com/@a6d70ece-69cf-4855-a63d-da6f79143fbd/projects/pwhmecwvqf?start=2023-12-09&amp;end=2023-12-15</a><br></p>
</td></tr>
</table></td></tr>
</table></td></tr> 
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-2-api-project/grade/psk" target="_blank">Grading</a></td></tr></table>