# Day 5: Dynamic Amplification Factor (DAF)

# Static result from Day 2
static_deflection = 0.004221627928995934  # m

# Dynamic result from Day 4
dynamic_deflection = 0.002972985372195997  # m

DAF = abs(dynamic_deflection) / abs(static_deflection)

print("Static deflection =", static_deflection, "m")
print("Dynamic deflection =", dynamic_deflection, "m")
print("Dynamic Amplification Factor (DAF) =", DAF)
