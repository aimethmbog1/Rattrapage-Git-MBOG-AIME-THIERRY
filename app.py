import gradio as gr

def hello(name):
    return f"Déploiement automatique réussi depuis GitHub Actions vers Hugging Face Spaces, {name} !"

demo = gr.Interface(fn=hello, inputs="text", outputs="text", title="Démonstration CI/CD - Rattrapage Git")

if __name__ == "__main__":
    demo.launch()
