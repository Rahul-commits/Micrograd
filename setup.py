import setuptools

setuptools.setup(
    name="micrograd",
    version="0.1.0",
    author="Rahul Narramneni",
    author_email="rahul.narramaneni@gmail.com",
    description="A tiny scalar-valued autograd engine with a small PyTorch-like neural network library on top.",
    url="https://github.com/karpathy/micrograd",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)