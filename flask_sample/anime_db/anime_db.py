from flask import Blueprint, flash, render_template, request, redirect, url_for, session
from sql.db import DB
from anime_db.forms import anime_db_Form, anime_db_FetchForm, anime_db_SearchForm, adminanime_db_SearchForm, anime_db_AssocForm
from roles.permissions import admin_permission
from flask_login import login_user, login_required, logout_user, current_user
from utils.lazy import DictToObject

anime_db = Blueprint('anime_db', __name__, url_prefix='/anime_db', template_folder='templates')

def get_status():
    results = DB.selectAll("SELECT DISTINCT status as label FROM IS601_Anime WHERE status != ''")
    r = []
    if results.status and results.rows:
        r = results.rows
    return r

def get_ranking():
    results = DB.selectAll("SELECT DISTINCT ranking as label FROM IS601_Anime WHERE ranking != ''")
    r = []
    if results.status and results.rows:
        r = results.rows
    return r

# insert_query = """INSERT INTO IS601_Anime 
#                     (anime_id, title, alternative_titles, genres, status, episodes, anime_type, ranking)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
#                 ON DUPLICATE KEY UPDATE
#                     title = VALUES(title),
#                     alternative_titles = VALUES(alternative_titles),
#                     genres = VALUES(genres),
#                     status = VALUES(status),
#                     episodes = VALUES(episodes),
#                     anime_type = VALUES(anime_type),
#                     ranking = VALUES(ranking)
#                 """

def get_total(partial_query, args={}):
    total = 0
    try:
        print("\n", "\nTotal QUERY -->", "SELECT count(1) as total FROM "+partial_query)
        result = DB.selectOne("SELECT count(1) as total FROM "+partial_query, args)
        print("\n", "\n Total ->", result)
        if result.status and result.row:
            total = int(result.row["total"])
    except Exception as e:
        print("\n", f"Error getting total {e}")
        total = 0
    return total

# psk 12/13/2023
@anime_db.route("/fetch", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def fetch():
    form = anime_db_FetchForm()
    if form.validate_on_submit():
        try:
            from utils.anime_db_api import Anime
            
            page_number = form.page_number.data
            page_size = form.page_size.data

            # Get a list of anime with pagination
            result_anime_db = Anime().get_anime(page=page_number, page_size=page_size)
            
            print(result_anime_db)
            # result_anime_db = Anime().get_anime(page=page_number, page_size=page_size)

            count = 0

            if 'data' in result_anime_db and result_anime_db['data']:
                for anime_data in result_anime_db['data']:
                    api_id = anime_data['_id']
                    title = anime_data['title']
                    alternative_titles = anime_data['alternativeTitles'][0]
                    ranking = anime_data['ranking']
                    genres = anime_data['genres'][0]
                    episodes = anime_data['episodes'] if 'episodes' in anime_data else None
                    status = anime_data['status']
                    anime_type = anime_data['type']

                    # Add the SQL query for insertion
                    result = DB.insertOne(
                        """INSERT INTO IS601_Anime (api_id,
                        title, alternativeTitles, ranking, genres, episodes, status, type)
                        VALUES (%s,%s, %s, %s, %s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE
                        api_id = VALUES(api_id),
                        title = VALUES(title),
                        alternativeTitles = VALUES(alternativeTitles),
                        ranking = VALUES(ranking),
                        genres = VALUES(genres),
                        episodes = VALUES(episodes),
                        status = VALUES(status),
                        type = VALUES(type)""",
                        api_id,title, alternative_titles, ranking, genres, episodes, status, anime_type
                    )

                    if result.status:
                        count += 1

                flash(f"Loaded {count} anime records.", "success")
            else:
                flash("No anime data found in the API response.", "danger")
            
        except Exception as e:
            flash(f"Error loading anime records: {e}", "danger")
    return render_template("anime_db_Fetch.html", form=form)

# psk 12/13/2023
@anime_db.route("/list", methods=["GET"])
def list():
    form = anime_db_SearchForm(request.args)

    
    # query = "SELECT id, api_id,title, alternativeTitles, ranking, genres, episodes, status, type FROM IS601_Anime WHERE 1=1"
    
    # Use request.args to get the parameters from the query string
    page_number = request.args.get("page_number", default=1, type=int)
    page_size = request.args.get("page_size", default=10, type=int)
    id = current_user.get_id()

    # # Add similar conditions for other fields...
    # status = [(k["label"],k["label"]) for k in get_status()]
    # status = [('', 'Not Selected')] + status
    # form.status.choices = status
    
    # ranking = [(k["label"],k["label"]) for k in get_ranking()]
    # ranking = [('', 'Not Selected')] + ranking
    # form.ranking.choices = ranking

    # allowed_columns = ["title", "alternativeTitles", "status", "ranking"]
    # form.sort.choices = [(k,k.title().replace("_", " ")) for k in allowed_columns]

    # if form.title.data:
    #     query += " AND title LIKE %(title)s"
    #     args["title"] = f"%{form.title.data}%"
        
    # if form.alternativeTitles.data:
    #     query += " AND alternativeTitles LIKE %(alternativeTitles)s"
    #     args["alternativeTitles"] = f"%{form.alternativeTitles.data}%"

    #     if form.status.data:
    #     query += " AND status LIKE %(status)s"
    #     args["status"] = f"%{form.status.data}%"
    
    # # if form.episodes.data:
    # #     query += " AND episodes LIKE %(episodes)s"
    # #     args["episodes"] = f"%{form.episodes.data}%"
        
    # # if form.type.data:
    # #     query += " AND type LIKE %(type)s"
    # #     args["type"] = f"%{form.type.data}%"
        
    # # if form.duration.data:
    # #     query += " AND duration LIKE %(duration)s"
    # #     args["duration"] = f"%{form.duration.data}%"
        
    # if form.ranking.data:
    #     query += " AND ranking LIKE %(ranking)s"
    #     args["ranking"] = f"%{form.ranking.data}%"
    
    # if form.sort.data in allowed_columns and form.order.data in ["asc", "desc"]:
    #     query += f" ORDER BY {form.sort.data} {form.order.data}"
    
    # if form.limit.data:
    #     if form.limit.data >100 or form.limit.data<1:
    #         form.limit.data = 10
    #         query += f" LIMIT 10"
    #     else:
    #         query += f" LIMIT {form.limit.data}"
    # else:
    #     query += f" LIMIT 10"

    # print("\n", "->", query, args)
    # rows = []
    try:
        result = DB.selectAll("SELECT id, api_id,title, alternativeTitles, ranking, genres, episodes, status, type FROM IS601_Anime WHERE 1=1")
        if result.status and result.rows:
            rows = result.rows

        total_records = get_total("IS601_Anime")

    except Exception as e:
        print("\n", e)
        flash("Error getting anime records", "danger")
        rows = []
        total_records = 0

    return render_template("anime_list.html", rows=rows, form=form, total_records=total_records)

# psk 12/13/2023
@anime_db.route("/add", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def add():
    form = anime_db_Form()
    if form.validate_on_submit():
        try:
            # Check for an existing record in IS601_Anime
            query = """
                SELECT title, status, ranking
                FROM IS601_Anime
                WHERE LOWER(title) = %(title)s
                  AND LOWER(status) = %(status)s
                  AND ranking = %(ranking)s
            """
            existing_result = DB.selectAll(query, {
                'title': form.title.data.lower(),
                'status': form.status.data.lower(),
                'ranking': form.ranking.data
            })

            if existing_result.status and existing_result.rows:
                flash("Anime record already exists", "warning")
            else:
                # Create a new anime record in the database
                insert_query = """
                    INSERT INTO IS601_Anime 
                    (title, alternativeTitles, genres, status, episodes, type,ranking) 
                    VALUES (%(title)s, %(alternativeTitles)s, %(genres)s, %(status)s, %(episodes)s, %(type)s, %(ranking)s)
                    ON DUPLICATE KEY UPDATE
                        title = VALUES(title),
                        alternativeTitles = VALUES(alternativeTitles),
                        genres = VALUES(genres),
                        status = VALUES(status),
                        episodes = VALUES(episodes),
                        type = VALUES(type),
                        ranking = VALUES(ranking)
                """
                insert_data = {
                    'title': form.title.data,
                    'alternativeTitles': form.alternative_titles.data,
                    'genres': form.genres.data,
                    'status': form.status.data,
                    'episodes': form.episodes.data,
                    'type': form.type.data,
                    'ranking': form.ranking.data
                }

                result = DB.insertOne(insert_query, insert_data)

                if result.status:
                    flash(f"Created anime record for {form.title.data}", "success")

        except Exception as e:
            flash(f"Error: {e}", "danger")

    return render_template("anime_form.html", form=form, type="Create")

# psk 12/13/2023
@anime_db.route("/edit", methods=["GET","POST"])
@admin_permission.require(http_exception=403)
def edit():
    id = request.args.get("id")
    if not id:
        flash("Missing ID", "danger")
        return redirect(url_for("anime_db.list"))
    
    form = anime_db_Form()
    
    # status = [(k["label"],k["label"]) for k in status()]
    # form.status.choices = status
    
    # ranking = [(k["label"],k["label"]) for k in ranking()]
    # form.ranking.choices = ranking
    
    if form.validate_on_submit():
        data = form.data
        # convert form data into query args dict
        del data["submit"]
        del data["csrf_token"]
        
        try:
            # print("\n", form.title.data.lower(), form.title_type.data.lower(), form.release_date.data)
            query = """
                    SELECT api_id, title, alternativeTitles, genres, status, episodes, type, ranking
                    FROM IS601_Anime 
                    WHERE LOWER(title) = %(title)s
                    AND LOWER(alternativeTitles) = %(alternativeTitles)s
                    AND LOWER(genres) = %(genres)sT
                    AND LOWER(status) = %(status)s
                    AND episodes = %(episodes)s
                    AND LOWER(type) = %(type)s
                    AND LOWER(ranking) = %(ranking)s
                """
                
            query_params = {
                'title': form.title.data.lower(),
                'alternativeTitles': form.alternative_titles.data.lower(),
                'genres': form.genres.data.lower(),
                'status': form.status.data.lower(),
                'episodes': form.episodes.data,
                'type': form.anime_type.data.lower(),
                'ranking': form.ranking.data.lower(),
            }
            
            print("\n", query)
            result = DB.selectAll(query, query_params)
            # print("\n", result)
            if result.status and result.rows[0]:
                flash("Anime record already exists","warning")
        except Exception as e:
            print("\n", e)      
            try:
                result = DB.insertOne("""
                    UPDATE IS601_Anime 
                    SET title = %s, alternativeTitles = %s, genres = %s, status = %s, 
                    episodes = %s, type = %s, ranking = %s 
                    WHERE id = %s""",
                    form.title.data, form.alternative_titles.data, form.genres.data, form.status.data, 
                    form.episodes.data, form.anime_type.data, form.ranking.data, 
                    id
                ) 
                if result.status:
                    flash(f"Updated anime record for {form.title.data}", "success")
            except Exception as e:
                flash(f"Error updating anime record: {e}", "danger")
    
    else:
        print("\n", "Form Errors:", form.errors)
        if len(form.errors) >0:
            return render_template("anime_form.html", form=form, type="Edit")
                    
    try:
        result = DB.selectOne("""
            SELECT api_id, title, alternativeTitles, genres, status, episodes, type, ranking
            FROM IS601_Anime 
            WHERE id = %s""",
            id
        )
        if result.status and result.row:
            data = DictToObject(result.row)
            form.process(obj=data)
        print("\n", f"Loaded form: {form.data}")
    except Exception as e:
        print(e)
        flash("Error fetching anime record", "danger")
        
    return render_template("anime_form.html", form=form, type="Edit")

# psk 12/13/2023
@anime_db.route("/delete", methods=["GET"])
@admin_permission.require(http_exception=403)
def delete():
    id = request.args.get("id")
    if not id:
        flash("Missing ID", "danger")
    else:
        args = {**request.args}
        print("\n", "->",args)
        del args["id"]
        result = DB.delete("DELETE FROM IS601_Anime WHERE id = %s", id)
        if result.status:
            flash("Deleted anime record", "success")
    return redirect(url_for("anime_db.list", **args))

# psk 12/13/2023
@anime_db.route("/view", methods=["GET"])
@login_required
def view():
    id = request.args.get("id")
    args = {**request.args}
    if not id:
        flash("Missing ID", "danger")
        return redirect(url_for("anime_db.list"))

    try:
        result = DB.selectOne("""
            SELECT api_id, title, alternativeTitles, genres, status, episodes, type, ranking,
            IFNULL((SELECT count(1) FROM IS601_Anime_list WHERE user_id = %(user_id)s), 0) as 'is_assoc' 
            FROM IS601_Anime WHERE id = %(anime_id)s""",
            {"user_id": current_user.id, "anime_id": id}
        )

        if result.status and result.row:
            return render_template("anime_view.html", anime_db=result.row)
        else:
            flash("Anime record not found", "danger")
    except Exception as e:
        print ("********************************************")
        print(e)
        flash("Error viewing anime record", "danger")

    return redirect(url_for("anime_db.list", **args))

# psk 12/13/2023
@anime_db.route("/track", methods=["GET"])
@login_required
def track():
    id = request.args.get("id")
    args = {**request.args}
    user_id = current_user.get_id()

    if id:
        
        try:
            try:
                result = DB.insertOne("INSERT INTO IS601_Anime_list (anime_id, user_id) VALUES (%(anime_id)s, %(user_id)s)", {'anime_id':id, 'user_id' : user_id})  # Update table title
                if result.status:
                    flash("Added anime to your watch list", "success")
            except Exception as e:
                print("\n", f"Should just be a duplicate exception and can be ignored {e}")
                result = DB.delete("DELETE FROM IS601_Anime_list WHERE anime_id = %(anime_id)s AND user_id = %(user_id)s", id,user_id)  # Update table title
                if result.status:
                    flash("Removed anime from your watch list", "success")
        except Exception as e:
            print("\n", f"Error doing something with 'Add to Watchlist'/'Remove from Watchlist' {e}")
            flash("An unhandled error occurred please try again", "danger")
    # if "source" in args and args["source"] == "view":
    #     args["id"] = id
    #     del args["source"]
    #     return redirect(url_for("anime_db.view", **args))
    # return redirect(url_for("anime_db.list", **args))
    else:
        flash("Missing id parameter", "danger")
    url = request.referrer
    if url:
        from urllib.parse import urlparse
        url_stuff = urlparse(url)
        watchlist_url = url_for("anime_db.watchlist")
        print("\n", f"Parsed url {url_stuff} {watchlist_url}")
        if url_stuff.path == url_for("anime_db.watchlist"):
            return redirect(url_for("anime_db.watchlist", **args))
        elif url_stuff.path == url_for("anime_db.view"):
            args["id"] = id
            return redirect(url_for("anime_db.view", **args))
    return redirect(url_for("anime_db.list", **args))

# psk 12/13/2023
@anime_db.route("/watchlist", methods=["GET"])
@login_required
def watchlist():
    id = request.args.get("id", current_user.id)
    args = {**request.args}
    
    form = anime_db_SearchForm(request.args)
    
    query = """
    SELECT a.id, title, alternativeTitles, genres, status, episodes, type, ranking, 1 as 'is_assoc'
    FROM IS601_Anime a JOIN IS601_Anime_list w ON a.id = w.anime_id
    WHERE w.user_id = %(user_id)s
    """
    
    args = {"user_id": id}
    
    # status = [(k["label"],k["label"]) for k in status()]
    # status = [('', 'Not Selected')] + status
    # form.status.choices = status
    
    # ranking = [(k["label"],k["label"]) for k in ranking()]
    # ranking = [('', 'Not Selected')] + ranking
    # form.ranking.choices = ranking
    
    # ["title", "alternative_titles", "genres", "status", "episodes", "anime_type", "ranking"]
    # allowed_columns = ["title", "alternative_titles", "status", "ranking"]
    # form.sort.choices = [(k,k.title().replace("_", " ")) for k in allowed_columns]
    
    if form.title.data:
        query += " AND title LIKE %(title)s"
        args["title"] = f"%{form.title.data}%"
        
    if form.alternative_titles.data:
        query += " AND alternativeTitles LIKE %(alternativeTitles)s"
        args["alternative_titles"] = f"%{form.alternative_titles.data}%"
        
    if form.status.data:
        query += " AND status LIKE %(status)s"
        args["status"] = f"%{form.status.data}%"
    
    if form.ranking.data:
        query += " AND ranking LIKE %(ranking)s"
        args["ranking"] = f"%{form.ranking.data}%"
    
    print("\n", "->", query, args)
    rows = []
    try:
        result = DB.selectAll(query, args)
        if result.status and result.rows:
            rows = result.rows
        total_records = get_total(""" IS601_Anime a JOIN IS601_Anime_list w ON a.id = w.anime_id WHERE w.user_id = %(user_id)s""", {"user_id": id})
        print("\n", "total_records->",total_records)

    except Exception as e:
        print("\n", e)
        flash(f"Error getting anime records: {e}", "danger")
    # return render_template("anime_list.html", rows=rows, form=form, title="Watchlist")
    return render_template("anime_list.html", rows=rows, form=form, title="Watchlist", total_records=total_records)


@anime_db.route("/clear", methods=["GET"])
@login_required
def clear():
    id = request.args.get("id")
    args = {**request.args}
    if "id" in args:
        del args["id"]
    if not id:
        flash("Missing id", "danger")
    else:
        # print()
        if id == current_user.get_id() or id == current_user.has_role("Admin"):
            try:
                result = DB.delete("DELETE FROM IS601_Anime_list WHERE user_id = %(user_id)s", {"user_id":id})
                if result.status:
                    flash("Cleared watchlist", "success")
            except Exception as e:
                print("\n", f"Error clearing watchlist {e}")
                flash("Error clearing watchlist","danger");
        

    return redirect(url_for("anime_db.watchlist", **args))

@anime_db.route("/associations", methods=["GET"])
@admin_permission.require(http_exception=403)
def associations():
    id = request.args.get("id", current_user.id)
    # args = {**request.args}
    
    form = adminanime_db_SearchForm(request.args)
    
    query = """
    SELECT u.id as user_id, a.id, title, alternativeTitles, genres, status, episodes, type, ranking
    FROM IS601_Anime a JOIN IS601_Anime_list w ON a.id = w.anime_id LEFT JOIN IS601_Users u on u.id = w.user_id
    WHERE 1=1
    """
    
    args = {}
    
    # status = [(k["label"],k["label"]) for k in status()]
    # status = [('', 'Not Selected')] + status
    # form.status.choices = status
    
    # ranking = [(k["label"],k["label"]) for k in ranking()]
    # ranking = [('', 'Not Selected')] + ranking
    # form.ranking.choices = ranking
    
    # ["title", "alternative_titles", "genres", "status", "episodes", "anime_type", "ranking"]
    # allowed_columns = ["title", "alternative_titles", "status", "ranking"]
    # form.sort.choices = [(k,k.title().replace("_", " ")) for k in allowed_columns]
    
    # if form.usertitle.data:
    #     args["usertitle"] = f"%{form.usertitle.data}%"
    #     query += " AND usertitle LIKE %(usertitle)s"
        
    if form.title.data:
        query += " AND title LIKE %(title)s"
        args["title"] = f"%{form.title.data}%w"
        
    if form.alternative_titles.data:
        query += " AND alternativeTitles LIKE %(alternativeTitles)s"
        args["alternativeTitles"] = f"%{form.alternative_titles.data}%"
        
    if form.status.data:
        query += " AND status LIKE %(status)s"
        args["status"] = f"%{form.status.data}%"
        
    if form.ranking.data:
        query += " AND ranking LIKE %(ranking)s"
        args["ranking"] = f"%{form.ranking.data}%"
    

    print("\n", "ASSOCIATIONS->", query, args)
    rows = []
    # total_records = 0
    try:
        total_records = get_total(""" IS601_Anime a JOIN IS601_Anime_list w ON a.id = w.anime_id WHERE w.user_id = %(user_id)s """, {"user_id": id})
        print("\n", "::::::::::::::::",query,args)
        result = DB.selectAll(query, args)
        
        print("\n", "result query associations->", result)
        if result.status and result.rows:
            rows = result.rows
        

    except Exception as e:
        print("\n", e)
        flash("Error getting anime records", "danger")
    # return render_template("anime_list.html", rows=rows, form=form, total_records=total_records)
    return render_template("anime_list.html", rows=rows, form=form, title="Associations", total_records=total_records)

# psk 12/13/2023
@anime_db.route("/unwatched", methods=["GET"])
@login_required
def unwatched():
    id = request.args.get("id", current_user.id)
    # args = {**request.args}
    
    form = anime_db_SearchForm(request.args)
    
    query = """
    SELECT a.id, title, alternativeTitles, genres, status, episodes, type, ranking,
    IFNULL((SElECT count(1) FROM IS601_Anime_list WHERE user_id = %(user_id)s and anime_id = a.id), 0) as 'is_assoc' 
    FROM IS601_Anime a
    WHERE a.id not in (SELECT DISTINCT anime_id FROM IS601_Anime_list)
    """
    
    args = {"user_id": id}
    
    # status = [(k["label"],k["label"]) for k in status()]
    # status = [('', 'Not Selected')] + status
    # form.status.choices = status
    
    # ranking = [(k["label"],k["label"]) for k in ranking()]
    # ranking = [('', 'Not Selected')] + ranking
    # form.ranking.choices = ranking
    
    # # ["title", "alternative_titles", "genres", "status", "episodes", "anime_type", "ranking"]
    # allowed_columns = ["title", "alternative_titles", "status", "ranking"]
    # form.sort.choices = [(k,k.title().replace("_", " ")) for k in allowed_columns]
    
    if form.title.data:
        query += " AND title LIKE %(title)s"
        args["title"] = f"%{form.title.data}%"
        
    if form.alternative_titles.data:
        query += " AND alternativeTitles LIKE %(alternativeTitles)s"
        args["alternativeTitles"] = f"%{form.alternative_titles.data}%"
        
    if form.status.data:
        query += " AND status LIKE %(status)s"
        args["status"] = f"%{form.status.data}%"
        
    if form.ranking.data:
        query += " AND ranking LIKE %(ranking)s"
        args["ranking"] = f"%{form.ranking.data}%"
    
    # if form.sort.data in allowed_columns and form.order.data in ["asc", "desc"]:
    #     query += f" ORDER BY {form.sort.data} {form.order.data}"
    
    # if form.limit.data:
    #     if form.limit.data >100 or form.limit.data<1:
    #         form.limit.data = 10
    #         query += f" LIMIT 10"
    #     else:
    #         query += f" LIMIT {form.limit.data}"
    # else:
    #     query += f" LIMIT 10"

    print("\n", "\nUNWATCHED (QUERY, ARGS)->", query, args)
    rows = []
    # total_records = 0
    try:
        total_records = get_total(""" IS601_Anime a WHERE a.id not in (SELECT DISTINCT anime_id FROM IS601_Anime_list)""")
        
        result = DB.selectAll(query, args)
        print("\n", "\nresult query unwatched->", result)
        
        if result.status and result.rows:
            rows = result.rows
        
    except Exception as e:
        print("\n", e)
        flash("Error getting anime records", "danger")
        
    return render_template("anime_list.html", rows=rows, form=form, title="Anime UnWatched", total_records=total_records)

# psk 12/13/2023
@anime_db.route("/manage", methods=["GET"])
@admin_permission.require(http_exception=403)
def manage():
    id = request.args.get("id", current_user.id)
    args = {**request.args}
    
    form = anime_db_AssocForm(request.args)
    
    users = []
    animes = []
    
    username = form.username.data
    anime_title = form.anime_db.data
    
    if username and anime_title:
        result = DB.selectAll("SELECT id, email FROM IS601_Users WHERE email like %(username)s LIMIT 25",{"username":f"%{username}%"})
        if result.status and result.rows:
            users = result.rows
        result = DB.selectAll("SELECT id, title FROM IS601_Anime WHERE title like %(anime_title)s LIMIT 25", {"anime_title":f"%{anime_title}%"})
        if result.status and result.rows:
            animes = result.rows
            
    print(f"Users {users}")
    print(f"animes {animes}")
    
    return render_template("anime_association.html", users=users, animes=animes, form=form)

# psk 12/13/2023
@anime_db.route("/manage_assoc", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def manage_assoc():
    users = request.form.getlist("users[]")
    animes = request.form.getlist("animes[]")
    
    print("\n users, animes -->", users, animes)
    
    args = {**request.args}
    
    if users and animes: # we need both for this to work
        mappings = []
        for user in users:
            for anime in animes:
                mappings.append({"user_id":user, "anime_id":anime})
        if len(mappings) > 0:
            for mapping in mappings:
                print(f"mapping {mapping}")
                try:
                    result = DB.insertOne("INSERT INTO IS601_Anime_list (user_id, anime_id) VALUES(%(user_id)s, %(anime_id)s)", mapping)
                    if result.status:
                        pass
                        #flash(f"Successfully enabled/disabled roles for the user/role {len(mappings)} mappings", "success")
                except Exception as e:
                    print(f"Insert error {e}")
                    result = DB.delete("DELETE FROM IS601_Anime_list WHERE user_id = %(user_id)s and anime_id = %(anime_id)s",mapping)
            flash("Successfully applied mappings", "success")
        else:
            flash("No user/anime mappings", "danger")

    if "users" in args:
        del args["users"]
    if "animes" in args:
        del args["animes"]
    return redirect(url_for("anime_db.manage", **args))
