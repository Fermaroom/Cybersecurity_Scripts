<#ESTRELLA MAYRANI DIAZ RODRIGUEZ
MARIA FERNANDA MACIAS ROMO
EDGAR RODRIGUEZ PEREZ#>

#script para obtener información de los servicios
Get-Service | Select-Object Name, Status, StartType, DisplayName `
| Export-CSV -NoTypeInformation -Path "services.csv" -Encoding UTF8