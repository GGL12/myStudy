//package AsyncIO;
//
//import org.apache.flink.configuration.Configuration;
//import org.apache.flink.streaming.api.functions.async.ResultFuture;
//import org.apache.flink.streaming.api.functions.async.RichAsyncFunction;
//import org.apache.http.HttpResponse;
//import org.apache.http.client.config.RequestConfig;
//import org.apache.http.client.methods.HttpGet;
//import org.apache.http.impl.nio.client.CloseableHttpAsyncClient;
//import org.apache.http.impl.nio.client.HttpAsyncClients;
//import org.apache.http.util.EntityUtils;
//import projectFlink.associatedData.ActivityBean;
//
//import java.util.Collections;
//import java.util.concurrent.CompletableFuture;
//import java.util.concurrent.Future;
//import java.util.function.Supplier;
//
//public class AsyncGeoToActivityBeanFunction extends RichAsyncFunction<String, ActivityBean> {
//    private transient CloseableHttpAsyncClient httpclient = null;
//
//    @Override
//    public void open(Configuration parameters) throws Exception {
//        super.open(parameters);
//        //初始化异步的httpclient
//        RequestConfig requestConfig = RequestConfig.custom()
//                .setConnectTimeout(50000)
//                .setSocketTimeout(50000)
//                .setConnectionRequestTimeout(10)//设置为10ms
//                .build();
//
//        httpclient = HttpAsyncClients.custom()
//                .setMaxConnTotal(20)
//                .setDefaultConnectionConfig(requestConfig)
//                .build();
//        httpclient.start();
//
//
//    }
//
//    @Override
//    public void asyncInvoke(String line, ResultFuture<ActivityBean> resultFuture) throws Exception {
//
//        String[] fields = line.split(",");
//        String uid = fields[0];
//        String aid = fields[1];
//        String time = fields[2];
//        int eventType = Integer.parseInt(fields[3]);
//        String longitude = fields[4];
//        String latitude = fields[5];
//
//        String url = "";
//        HttpGet httpGet = new HttpGet(url);
//        Future<HttpResponse> future = httpclient.execute(httpGet, null);
//        CompletableFuture.supplyAsync(new Supplier<String>() {
//            @Override
//            public String get() {
//                HttpResponse response = null;
//                try {
//                    response = future.get();
//                    String res = null;
//                    if (response.getStatusLine().getStatusCode() == 200) {
//                        res = EntityUtils.toString(response.getEntity());
//                    }
//                    return res;
//                } catch (Exception e) {
//                    return null;
//                }
//            }
//        }).thenAccept((String province) -> {
//            resultFuture.complete(Collections.singleton(ActivityBean.of(uid, aid, null, time, eventType, province)));
//        });
//    }
//
//    @Override
//    public void close() throws Exception {
//        super.close();
//        httpclient.close();
//    }
//}
