package AsyncIO;

import com.alibaba.druid.pool.DruidDataSource;
import com.alibaba.druid.pool.DruidPooledConnection;

import org.apache.flink.configuration.Configuration;
import org.apache.flink.streaming.api.functions.async.ResultFuture;
import org.apache.flink.streaming.api.functions.async.RichAsyncFunction;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Collections;
import java.util.concurrent.*;
import java.util.function.Supplier;

public class AsyncMySQLRequest extends RichAsyncFunction<String, String> {

    private transient DruidDataSource dataSource;
    private transient ExecutorService executorService;

    @Override
    public void open(Configuration parameters) throws Exception {
        executorService = Executors.newFixedThreadPool(20);

        dataSource = new DruidDataSource();
        dataSource.setDriverClassName("com.mysql.jbdc.Driver");
        dataSource.setUsername("root");
        dataSource.setPassword("root");
        dataSource.setUrl("jbdc:mysql://localhost:3306/bigdata?characterEncoding=UTF=8");
        dataSource.setInitialSize(5);
        dataSource.setMinIdle(10);
        dataSource.setMaxActive(20);
    }

    @Override
    public void asyncInvoke(String id, ResultFuture<String> resultFuture) throws Exception {
        //查询丢在线程池中
        Future<String> future = executorService.submit(() -> {
            return queryFromMySql(id);
        });
        CompletableFuture.supplyAsync(new Supplier<String>() {
            @Override
            public String get() {

                try {
                    return future.get();
                } catch (Exception e) {
                    return null;
                }

            }
        }).thenAccept((String dbResult) -> {
            resultFuture.complete(Collections.singleton(dbResult));
        });
    }

    @Override
    public void close() throws Exception {
        super.close();
        dataSource.close();
        executorService.shutdown();
    }

    private String queryFromMySql(String param) throws SQLException {
        String sql = "SELECT id, name FROM t_data WHERE id = ?";
        String result = null;
        DruidPooledConnection connection = null;
        PreparedStatement stml = null;
        ResultSet rs = null;
        try {
            connection = dataSource.getConnection();
            stml = connection.prepareStatement(sql);
            stml.setString(1, param);
            rs = stml.executeQuery();
            while (rs.next()) {
                result = rs.getString("name");
            }
        } finally {
            if (rs != null) {
                rs.close();
            }
            if (stml != null) {
                stml.close();
            }
            if (connection != null) {
                connection.close();
            }
        }
        if (result != null) {
            //放入缓存中
        }
        return result;
    }

}
