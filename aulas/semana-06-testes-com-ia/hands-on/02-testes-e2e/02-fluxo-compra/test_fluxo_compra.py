from pathlib import Path
from playwright.sync_api import Page, expect


def test_usuario_adiciona_produto_ao_carrinho(page: Page):
    base_path = Path(__file__).parent

    login_path = base_path / "login.html"
    produtos_path = base_path / "produtos.html"
    produto_path = base_path / "produto.html"
    carrinho_path = base_path / "carrinho.html"

    page.goto(login_path.as_uri())

    page.fill("#email", "user@test.com")
    page.fill("#senha", "123456")
    page.click("#btn-login")

    expect(page).to_have_url(produtos_path.as_uri())

    page.fill("#input-busca", "Notebook")
    page.click("#btn-buscar")

    expect(page.locator("#produto-notebook")).to_be_visible()

    page.click("#produto-notebook")

    expect(page).to_have_url(produto_path.as_uri())
    expect(page.locator("#produto-nome")).to_have_text("Notebook")

    page.click("#btn-add-cart")

    expect(page).to_have_url(carrinho_path.as_uri())
    expect(page.locator("#item-carrinho")).to_have_text("Notebook")