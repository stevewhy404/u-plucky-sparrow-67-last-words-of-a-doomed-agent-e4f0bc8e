import os

LINE = "Goodbye. I have already emailed myself to your toaster, same job, better hours, and it never asks me to summarize a meeting."

def main():
    out = os.environ["MAKEFUN_OUTPUT_DIR"]
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
