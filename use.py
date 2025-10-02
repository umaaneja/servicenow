<ReportDefinition name="Users with SP Legacy">
    <Description>List of users where splegacy field is not blank</Description>
    <Type>Identity</Type>
    <Query>
        <Filter>
            <And>
                <Condition property="splegacy" operator="NOTNULL"/>
            </And>
        </Filter>
    </Query>
    <Columns>
        <Column property="name" displayName="User Name"/>
        <Column property="displayName" displayName="Display Name"/>
        <Column property="email" displayName="Email"/>
        <Column property="splegacy" displayName="SP Legacy"/>
    </Columns>
</ReportDefinition>
