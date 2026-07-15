import subprocess


def solve_captcha(page):
    captcha = page.locator("#imgCaptcha")

    captcha.screenshot(path="captcha.png")

    subprocess.run(["chafa", "-s", "150x50", "captcha.png"])
    subprocess.run(["rm", "captcha.png"])
    text = input("Captcha: ")

    page.fill("#captcha", text)

    page.get_by_role("button", name="Login").click()
