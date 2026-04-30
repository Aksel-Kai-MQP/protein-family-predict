import os
import matplotlib.pyplot as plt


def parse_xvg(filepath):
    x_data = []
    y_data = []
    with open(filepath, "r") as file:
        for line in file:
            if not line.startswith(("@", "#")):
                parts = line.split()
                if len(parts) >= 2:
                    try:
                        x_data.append(float(parts[0]))
                        y_data.append(float(parts[1]))
                    except ValueError:
                        continue
    return x_data, y_data


def format_species_name(species_str):
    mapping = {
        "mers_cov": "MERS-CoV",
        "sars_cov_1": "SARS-CoV-1",
        "sars_cov_2": "SARS-CoV-2",
        "human_coronavirus_hcov_hku1": "Human Coronavirus HCoV-HKU1",
        "bovine_coronavirus": "Bovine Coronavirus",
        "murine_coronavirus": "Murine Coronavirus",
        "template": "Template",
    }
    return mapping.get(species_str, species_str.replace("_", " ").title())


def main():
    metrics_info = {
        "rmsd": {
            "title_suffix": "RMSD",
            "x_label": "Time (ns)",
            "y_label": "RMSD (nm)",
        },
        "rmsf": {
            "title_suffix": "RMSF",
            "x_label": "Atom / Residue Index",
            "y_label": "RMSF (nm)",
        },
        "gyrate": {
            "title_suffix": "Radius of Gyration",
            "x_label": "Time (ns)",
            "y_label": "Radius of Gyration (nm)",
        },
    }

    files = [f for f in os.listdir(".") if f.endswith(".xvg")]

    for filename in files:
        if filename.endswith("_rmsd.xvg"):
            species_raw = filename[:-9]
            metric = "rmsd"
        elif filename.endswith("_rmsf.xvg"):
            species_raw = filename[:-9]
            metric = "rmsf"
        elif filename.endswith("_gyrate.xvg"):
            species_raw = filename[:-11]
            metric = "gyrate"
        else:
            print(f"Skipping {filename}: Does not match expected naming convention.")
            continue

        species_title = format_species_name(species_raw)
        plot_title = (
            f"{species_title} E Protein - {metrics_info[metric]['title_suffix']}"
        )
        x_label = metrics_info[metric]["x_label"]
        y_label = metrics_info[metric]["y_label"]

        output_dir = species_raw
        os.makedirs(output_dir, exist_ok=True)

        print(f"Processing {filename}...")
        x, y = parse_xvg(filename)

        if not x or not y:
            print(f"Warning: No data found in {filename}. Skipping plot.")
            continue

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, color="#1f77b4", linewidth=1.5)

        plt.title(plot_title, fontsize=14, fontweight="bold")
        plt.xlabel(x_label, fontsize=12)
        plt.ylabel(y_label, fontsize=12)
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.tight_layout()

        output_path = os.path.join(output_dir, f"{species_raw}_{metric}.png")
        plt.savefig(output_path, dpi=300)
        plt.close()

    print("All plots generated and saved successfully!")


if __name__ == "__main__":
    main()
