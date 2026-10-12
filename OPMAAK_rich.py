#https://calmcode.io/course/rich/main
from rich import style
from rich.console import Console
from rich.table import Table
from rich.theme import Theme
from rich.columns import Columns
from rich.panel import Panel
from rich.markdown import Markdown
from rich.align import Align  # om te centreren ed

console = Console()

#onderstaand wordt een tabel met kleuren, alle print het pas later in terminal??
print("OEFENING 1")
table = Table(title="Kleuren test")

table.add_column("Naam", style="bold cyan")
table.add_column("Leeftijd", style="magenta")
table.add_column("Kleur", style="green")

table.add_row("Jane", "28", "Blauw")
table.add_row("Mark", "34", "Groen")
print()
console.print(table)
print()
console.print("Hello, [bold magenta]World[/bold magenta]! :vampire:")
console.print(":smiley: :vampire: :pile_of_poo: :thumbs_up: :raccoon:")
print()
print()
console.print("Normale tekst")
console.print("Rode tekst", style="red")
console.print("Vet rood", style="bold red")
console.print("[bold green]Groen[/bold green]")
print()
print()
#OPMAAK THEME
print("OPMAAK THEME")
custom_theme = Theme({
    "good" : "green",
    "bad": "bold red"})

console = Console(theme=custom_theme)
console.print("File downloaded!", style="good")
console.print("File corrupted!", style="bad")
console.print("The internet is [bad]down![/bad]")
print()
print("OPMAAK TABEL PANDA")
print()
table = Table(title="Pandas Versions")

table.add_column("Released", style="cyan")
table.add_column("Version Number", justify="right", style="magenta")
table.add_column("Description", style="green")
table.add_column("status", style="violet")

table.add_row("May 29, 2020", "v1.0.4", "Just an update", "ok")
table.add_row("Mar 18, 2020", "v1.0.3", "Just an update.", "not ok")
table.add_row("Mar 15, 2020", "v1.0.2", "Just.", "dont know")
table.add_row("Oct 21, 2021", "v.0009", "ok", "archieved")
table.add_row("Feb 05, 2020", "v1.0.1", ":thumbs_up: [underline]Big[/] update.")
console.print(table)


# md1 = Dit is een multiline string. Alles tussen de drie aanhalingstekens """ wordt opgeslagen als tekst.

# Hoofdtitel
## Subtitel
### Kleinere titel
#Gewone tekst: """

md1 = """
# Hello World

## This is Markdown

de tekst is cursief en vetgedrukt *VERY* **NICELY**!
"""

md2 = """
## This is Markdown, Again

With code!

```python
print("hello world")
```
"""

console = Console(record=True)
panel_1 = Panel.fit(Align.center(Markdown(md1)), title="panel one")
panel_2 = Panel(Markdown(md2), title="panel two")

panel_1 = Panel.fit(Markdown(md1), title="panel one", width=30)
panel_2 = Panel.fit(Markdown(md2), title="panel two", width=30)
console.print(Align.center(Markdown("## This is Markdown, Again")))

console.print(Columns([panel_1, panel_2],equal=True))