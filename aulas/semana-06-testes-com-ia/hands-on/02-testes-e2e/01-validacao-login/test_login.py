from pathlib import Path
from playwright.sync_api import Page, expect


def test_login_redireciona_para_dashboard(page: Page):
    base = Path(__file__).parent
    page.goto((base / "login.html").as_uri())

    page.fill("#email", "user@test.com")
    page.fill("#senha", "123456")
    page.click("#btn-login")

    expect(page).to_have_url((base / "dashboard.html").as_uri())
    expect(page.locator("#btn-logout")).to_be_visible()
