from jinja2 import Template

def jinja_render():
    # 定义模板字符串
    template_str = "Hello, {{ name }}!"

    # 创建模板对象
    template = Template(template_str)

    # 渲染模板并传入变量
    output = template.render(name="World")
    print(output) 

def jinja_render_file():
    # 定义模板
    template = Template(open("/Users/wei.wang/workspacePy/pyExamples/jinja2/index.html").read())

    # 渲染模板
    output = template.render(name="John")

    # 打印生成的 HTML
    print(output)

if __name__ == "__main__":
    jinja_render()
    jinja_render_file()






