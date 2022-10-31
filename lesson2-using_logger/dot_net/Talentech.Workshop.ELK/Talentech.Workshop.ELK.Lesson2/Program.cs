using Serilog;
using Serilog.Events;
using Serilog.Formatting.Elasticsearch;
using Serilog.Sinks.Elasticsearch;

var logger = CreateLogger();

logger.Information("Hello, World!");

Log.CloseAndFlush();

ILogger CreateLogger()
{
    var elasticSearchURL = "http://localhost:9200/";

    var loggerBuilder = new LoggerConfiguration()
                .Enrich.FromLogContext()
                .Enrich.WithProperty("Platform", "Talentech")
                .Enrich.WithProperty("Solution", "Workshop")
                .Enrich.WithProperty("AppName", "Lesson2")
                .Enrich.WithProperty("EnvironmentName", "Local");

        loggerBuilder.WriteTo.Logger(
                l => l.WriteTo.Elasticsearch(
                        new ElasticsearchSinkOptions(new Uri(elasticSearchURL))
                        {
                            MinimumLogEventLevel = LogEventLevel.Information,
                            AutoRegisterTemplate = false,
                            IndexFormat = "talmundo-logs",
                            CustomFormatter = new ExceptionAsObjectJsonFormatter(renderMessage: true)
                        }));

    Log.Logger = loggerBuilder.CreateLogger();

    return Log.Logger;
} 