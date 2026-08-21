// Power Query M Script for Power BI Desktop
let
    SourceFact = Csv.Document(File.Contents("C:\Users\91638\Desktop\AIRLINE_DATA_ANALYTICS\data\processed\airline_cleaned.csv"),[Delimiter=",", Columns=39, Encoding=1252, QuoteStyle=QuoteStyle.None]),
    PromoteFactHeaders = Table.PromoteHeaders(SourceFact, [PromoteAllScalars=true])
in
    PromoteFactHeaders
