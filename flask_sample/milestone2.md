<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 API Project</td></tr>
<tr><td> <em>Student: </em> Pranav Kowadkar (psk)</td></tr>
<tr><td> <em>Generated: </em> 12/14/2023 10:51:50 PM</td></tr>
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
<table><tr><td> <em>Deliverable 2: </em> Create Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show the create page</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show the new data in the database</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/p-kowadkar/psk-IS601-007/pull/28">https://github.com/p-kowadkar/psk-IS601-007/pull/28</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> List Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707795-a9c94a71-7871-4572-bfae-ad636f8f8474.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page that lists the application entities (both API and custom)</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Include related pull request(s)</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> View Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707795-a9c94a71-7871-4572-bfae-ad636f8f8474.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page showing a single entity with more details shown</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Include related pull request(s)</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707795-a9c94a71-7871-4572-bfae-ad636f8f8474.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page to edit a single entity</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Database</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707795-a9c94a71-7871-4572-bfae-ad636f8f8474.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a route for deletion logic</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Database</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> API Data Loading </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show information related to API data loading</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe the process</td></tr>
<tr><td> <em>Response:</em> <p>(missing)</p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/p-kowadkar/psk-IS601-007/pull/29">https://github.com/p-kowadkar/psk-IS601-007/pull/29</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>(missing)</p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-psk-prod-1dc8f6f2f85b.herokuapp.com/login">https://is601-psk-prod-1dc8f6f2f85b.herokuapp.com/login</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Include Screenshots from Wakatime</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-2-api-project/grade/psk" target="_blank">Grading</a></td></tr></table>