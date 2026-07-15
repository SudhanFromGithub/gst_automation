# Importing Required Libraries
from playwright.sync_api import sync_playwright
from pathlib import Path
from rich import print
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn, TimeElapsedColumn
from rich.console import Console
import subprocess, os

outputfolder = Path.home() / "Desktop"
os.makedirs(outputfolder, exist_ok=True)

# Asks user to whether to run it headless
headless_user_input = input("Whether you want to run it windowless(yes/no)? : ").strip().lower()

console = Console()
username = input("Enter GST Username: ")
password = input("Enter GST Password: ")

def submit_captcha(page):
    page.wait_for_timeout(1000)
    captcha = page.locator("#imgCaptcha")
    captcha.screenshot(path="captcha.png")

    subprocess.run(["chafa", "-s", "150x50", "captcha.png"])
    
    captcha_text = input("Enter Captcha: ")
    page.fill("#captcha", "")  
    page.fill("#captcha", captcha_text)

    page.wait_for_timeout(1000)
    login_button = page.get_by_role("button", name="Login")
    login_button.click()


with sync_playwright() as p:
    
    #Runs in windowed/windowless based on user's input
    if headless_user_input == "yes":
        browser = p.chromium.launch(headless=True)
    else:
        browser = p.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto("https://services.gst.gov.in/services/login")

    page.fill("#username", username)

    while True:

        page.fill("#user_pass", password)

        submit_captcha(page)

        page.wait_for_timeout(2000)
        
        try:
            page.wait_for_selector(
            "text=Enter valid Letters shown",
            timeout=3000
            )
            print("Wrong captcha. Try again.")
            continue

        except:
            break

    print(f"[green]✓ Succesfully logged in[/green] ")
    Financial_Year = input("Enter FY Year of Returns:")

    #page.get_by_text("Remind me later").click()
    page.get_by_role("button", name="RETURN DASHBOARD").click()

    
    data = {
        "Quarter 1 (Apr - Jun)": ["April", "May", "June"],
        "Quarter 2 (Jul - Sep)": ["July", "August", "September"],
        "Quarter 3 (Oct - Dec)": ["October", "November", "December"],
        "Quarter 4 (Jan - Mar)": ["January", "February", "March"]
    }

    total_months = sum(len(months) for months in data.values())

    counter = 1

    with Progress(
    SpinnerColumn(),
    TextColumn("[progress.description]{task.description}"),
    BarColumn(),
    TaskProgressColumn(),
    TimeElapsedColumn(),
    ) as progress:

        overall = progress.add_task("[cyan]Overall Progress", total=total_months)

        for Quarter, Months in data.items():

            for month in Months:
                
                month_task = progress.add_task(f"[yellow]{month}", total=5)
    
                # select Financial_Year
                page.select_option("select[name='fin']", label=Financial_Year)
                page.wait_for_timeout(2000)
                progress.advance(month_task)

                # select Quarter
                page.select_option("select[name='quarter']", label=Quarter)
                page.wait_for_timeout(2000)
                progress.advance(month_task)

                # select month
                page.select_option("select[name='mon']", label=month)
                page.wait_for_timeout(2000)
                progress.advance(month_task)

                # select Search button
                page.get_by_role("button", name="Search", exact=True).click()

                # Select View button in GSTR1
                page.get_by_role("button", name="VIEW", exact=True).click()

                # Select view summary button inside GSTR1
                #page.locator('xpath=/html/body/div[2]/div[2]/div/div[2]/div[7]/div/div/button[2]').click
                page.get_by_role("button", name="VIEW SUMMARY", exact=True).click()

                # Click download pdf button
                #page.locator("button[data-ng-click='genratepdfNew()']").click
                #page.locator('xpath=/html/body/div[2]/div[2]/div/div[2]/div[7]/div/button[3]')
                progress.advance(month_task)

                with page.expect_download() as download_info:

                    page.locator("button[data-ng-click='genratepdfNew()']").click()

                download = download_info.value
                download.save_as(f"{outputfolder}/{counter}.GSTR1_Summary_{month}.pdf")
                progress.advance(month_task)

                progress.print(f"[green]✓ Saved[/green] {counter}.GSTR1_Summary_{month}.pdf")
                counter += 1

                progress.advance(overall)


                page.get_by_role("button", name="Back", exact=True).click()

                page.locator("a[href='/returns/auth/dashboard']", has_text="Back").click()



        console.input("[red]Press enter to exit....[/red]")
    
    
    
