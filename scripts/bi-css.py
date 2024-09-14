#!/usr/bin/env python
import json
import time
import tinycss2

classes = json.load(open("./scripts/classes.json"))

cur_time = int(time.time())

rules = tinycss2.parse_stylesheet(
    open("./vgarchive/theme/static_src/src/bs-icons/bootstrap-icons.css").read(),
    skip_comments=True,
)

final_rules = rules[:4]

font_rule = rules[1]

for block in font_rule.content:
    if isinstance(block, tinycss2.ast.FunctionBlock):
        arg = block.arguments[0]
        arg.value += f"?v={cur_time}"
        arg.representation = arg.representation.replace(
            ".min.woff2", f".min.woff2?v={cur_time}"
        )
        block.arguments[0] = arg

rules = rules[4:]

for i, rule in enumerate(rules):
    if isinstance(rule, tinycss2.ast.WhitespaceToken):
        continue

    if rule.prelude[1].value not in classes:
        del rules[i]
    else:
        char = hex(ord(rule.content[4].value))[2:]
        rule.content[4].representation = f'"\\{char}"'
        final_rules.append(rule)
        final_rules.append(rules[i + 1])


out = open("./vgarchive/theme/static_src/src/bs-icons/bootstrap-icons.min.css", "w")
out.write(tinycss2.serialize(final_rules))
out.close()
