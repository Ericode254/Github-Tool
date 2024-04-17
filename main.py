import requests
import flet as flt

def github_function(name):
	username = name
	url = f"https://api.github.com/users/{username}"
	user_data = requests.get(url)
	data = user_data.json()

	return username, data["public_repos"], data["following"], data["html_url"]

def myapp(page: flt.Page):
	def go_to_profile(e):
		page.launch_url(url)

	def go_to_github(e):
		page.launch_url("https://github.com/")

	def submit(e):
		global url
		name, repos, folowers, url = github_function(text.value)
		page.title = f"GitHub information for {name}"
		page.add(
	        flt.Card(
	            content=flt.Container(
	                content=flt.Column(
	                    [
	                        flt.ListTile(
	                            leading=flt.Icon(flt.icons.ALBUM),
	                            title=flt.Text(name),
	                            subtitle=flt.Text(
	                                f"{name} has {folowers} followers and {repos} repositories"
	                            ),
	                        ),
	                        flt.Row(
	                            [flt.TextButton("Go to profile", on_click=go_to_profile), flt.TextButton("Go to github", on_click=go_to_github)],
	                            alignment=flt.MainAxisAlignment.END,
	                        ),
	                    ]
	                ),
	                width=400,
	                padding=10,
	            )
	        )
	    )

	page.theme_mode = flt.ThemeMode.DARK # change DARK to LIGHT to convert it to light mode
	page.window_height = 400
	page.window_width = 500

	page.title = 'GitHub Tool'

	text = flt.TextField(
            label = "Enter github username",
            suffix=flt.ElevatedButton("Submit", on_click=submit),
            on_submit=submit,
            border = flt.InputBorder.UNDERLINE
        )


	page.add(text)
	page.update()


flt.app(target=myapp)