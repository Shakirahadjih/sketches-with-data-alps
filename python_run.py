import matplotlib.pyplot as plt

from mean_global_tempchanges import global_years, global_anomalies
from swiss_global_tempchanges import switzerland_years, switzerland_anomalies

# Plotting the bar graph
plt.figure(figsize=(10, 6))

# Global temperature anomaly
plt.bar(global_years, global_anomalies, color='blue', label='Global')

# Switzerland temperature anomaly
plt.bar(switzerland_years, switzerland_anomalies, color='red', label='Switzerland')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly (°C)')
plt.title('Temperature Anomalies Relative to 1961-1990 Average Temperature')
plt.legend()

# Show plot
plt.tight_layout()
plt.show()