
class BarChartWidget(QWidget):
    def __init__(self, percentages):
        super().__init__()
        self.percentages = percentages
        self.initUI()

    def initUI(self):
        # Create a Figure object
        self.figure = Figure()

        # Create a FigureCanvas object and add it to the layout
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        # Plot the bar chart
        self.plot_bar_chart()

    def plot_bar_chart(self):
        ax = self.figure.add_subplot(111)
        ax.clear()

        # Set background color
        self.figure.patch.set_facecolor('black')
        ax.set_facecolor('black')

        # Create the bar chart
        categories = [f"C {i+1}" for i in range(len(self.percentages))]
        bar_colors = ['green' if p > 80 else 'red' for p in self.percentages]
        bars = ax.bar(categories, self.percentages, color=bar_colors)

        # Customize chart elements
        ax.set_ylim(0, 100)

        # Customize tick labels
        ax.tick_params(axis='x', colors='gray')
        ax.tick_params(axis='y', colors='gray')
        ax.set_xticklabels([])  # Remove x-axis tick labels

        # Customize spines
        ax.spines['bottom'].set_color('gray')
        ax.spines['top'].set_color('gray')
        ax.spines['left'].set_color('gray')
        ax.spines['right'].set_color('gray')

        # Draw the canvas
        self.canvas.draw()


    def update_chart(self, new_percentages):
        self.percentages = new_percentages
        self.plot_bar_chart()
